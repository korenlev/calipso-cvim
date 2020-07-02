###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import json
from http import HTTPStatus
from json import JSONDecodeError
from typing import Optional, Tuple, List
from urllib import parse

import re

import pymongo
from dateutil import parser
from pymongo import errors

from api.exceptions import exceptions
from api.validation.data_validate import DataValidate
from base.utils.dict_naming_converter import DictNamingConverter
from base.utils.inventory_mgr import InventoryMgr
from base.utils.logging.full_logger import FullLogger
from base.utils.string_utils import jsonify, stringify_doc


class ResponderBase(DataValidate, DictNamingConverter):
    UNCHANGED_COLLECTIONS = ["monitoring_config_templates",
                             "environments_config",
                             "messages",
                             "scheduled_scans"]
    ID = "_id"
    COLLECTION = None

    def __init__(self, log_file: Optional[str] = None, log_level: Optional[str] = None):
        super().__init__()
        self.log = FullLogger(name="API Responder", log_file=log_file, level=log_level)
        self.inv = InventoryMgr()

    ######################
    #     Responses      #
    ######################

    @staticmethod
    def _set_error_response(title="", code=HTTPStatus.BAD_REQUEST, message="", body=""):
        code = str(code.value)
        if body:
            raise exceptions.CalipsoApiException(code, body, message)

        body = jsonify({
            "error": {
                "message": message,
                "code": code,
                "title": title
            }
        })
        raise exceptions.CalipsoApiException(code, body, message)

    def _set_successful_response(self, resp, body: object = "", status=HTTPStatus.OK):
        if not isinstance(body, str):
            try:
                body = jsonify(body)
            except Exception as e:
                self.log.exception(e)
                raise ValueError("The response body should be a string")
        resp.status = str(status.value)
        resp.body = body

    def set_ok_response(self, resp, body: object = ""):
        return self._set_successful_response(resp, body, HTTPStatus.OK)

    def set_created_response(self, resp, body: object = ""):
        return self._set_successful_response(resp, body, HTTPStatus.CREATED)

    def bad_request(self, message="Invalid request content"):
        self._set_error_response("Bad Request", HTTPStatus.BAD_REQUEST, message)

    def unauthorized(self, message="Request requires authorization"):
        self._set_error_response("Unauthorized", HTTPStatus.UNAUTHORIZED, message)

    def not_found(self, message="Requested resource not found"):
        self._set_error_response("Not Found", HTTPStatus.NOT_FOUND, message)

    def conflict(self, message="The posted data conflicts with the existing data"):
        self._set_error_response("Conflict", HTTPStatus.CONFLICT, message)

    ######################
    # Query manipulation #
    ######################

    def validate_query_data(self, data: dict, data_requirements: dict,
                            additional_key_reg: Optional[str] = None,
                            can_be_empty_keys: Optional[list] = None) -> None:
        error_message = self.validate_data(data=data, requirements=data_requirements,
                                           additional_key_re=additional_key_reg,
                                           can_be_empty_keys=can_be_empty_keys)
        if error_message:
            self.bad_request(error_message)

    def parse_query_params(self, req):
        query_string = req.query_string
        if not query_string:
            return {}
        try:
            query_params = dict((k, v if len(v) > 1 else v[0])
                                for k, v in
                                parse.parse_qs(query_string,
                                               keep_blank_values=True,
                                               strict_parsing=True).items())
            return query_params
        except ValueError as e:
            self.bad_request(str("Invalid query string: {0}".format(str(e))))

    @staticmethod
    def update_query_with_filters(filters, filters_keys, query):
        query.update({k: filters[k] for k in filters_keys if filters.get(k)})

    def build_query(self, filters):
        query = {}
        _id = filters.get("id")
        if _id:
            query[self.ID] = _id
        query['environment'] = filters['env_name']
        return query

    @staticmethod
    def get_content_from_request(req):
        error = ""
        content = ""
        if not req.content_length:
            error = "No data found in the request body"
            return error, content

        data = req.stream.read()
        content_string = data.decode()
        try:
            content = json.loads(content_string)
            if not isinstance(content, dict):
                error = "The data in the request body must be an object"
        except (TypeError, JSONDecodeError):
            error = "The request can not be fulfilled due to bad syntax"

        return error, content

    ######################
    #     DB Helpers     #
    ######################

    def get_collection_by_name(self, name: str) -> pymongo.collection.Collection:
        if name in self.UNCHANGED_COLLECTIONS:
            return self.inv.db[name]
        return self.inv.collections[name]

    def get_constants_by_name(self, name: str, environment_type: str = None, environment_name: str = None) -> list:
        """

        :param name: constants object name
        :param environment_type: environment type to lookup constants for (mutually exclusive with env name)
        :param environment_name: environment to lookup constants for (mutually exclusive with env type)
        :return: list of strings
        """
        query = {"name": name}
        if environment_type:
            query["environment_type"] = environment_type
        elif environment_name:
            environment = self.get_single_object(collection="environments_config",
                                                 query={"name": environment_name})
            if not environment:
                self.bad_request("unknown environment: {}".format(environment_name))
            query["environment_type"] = environment["environment_type"]
        else:
            query["environment_type"] = {"$in": [None, "OpenStack"]}

        constants = self.distinct(collection="constants", field="data.value", query=query)
        if not constants:
            self.log.error('No constants with name "{}" exist'.format(name))

        return constants

    def check_environment_name(self, env_name: str) -> bool:
        query = {"name": env_name}
        objects = self.read(collection="environments_config", query=query)
        if not objects:
            return False
        return True

    def get_single_object(self, collection: str, query: dict, aggregate: Optional[list] = None) -> dict:
        env_name = query.get("environment")
        if env_name and not self.check_environment_name(env_name):
            self.bad_request("unknown environment: " + env_name)

        objs = self.read(collection=collection, query=query, aggregate=aggregate)
        if not objs:
            return {}

        obj = objs[0]
        stringify_doc(obj)
        if self.ID == "_id":
            obj['id'] = obj.get('_id')

        return obj

    def get_objects_list(self, collection: str, query: dict, page: int = 0, page_size: int = 1000,
                         projection: Optional[dict] = None, aggregate: Optional[list] = None,
                         sort: Optional[List[Tuple]] = None) -> list:
        env_name = query.get("environment")
        if env_name and not self.check_environment_name(env_name):
            self.bad_request("Unknown environment: {}".format(env_name))

        objects = self.read(collection=collection, query=query, projection=projection, aggregate=aggregate,
                            sort=sort, skip=page, limit=page_size)

        for obj in objects:
            if "id" not in obj and "_id" in obj:
                obj["id"] = str(obj.pop("_id"))

        stringify_doc(objects)
        return objects

    def delete_object_by_id(self, collection: str, query: dict):
        if self.ID not in query:
            self.bad_request("Object ID must be specified for deletion")

        env_name = query.get("environment")
        if not env_name or not self.check_environment_name(env_name):
            self.bad_request("Unknown environment: {}".format(env_name))

        return self.delete(collection, query, delete_one=True)

    def delete_objects(self, collection, query):
        env_name = query.get("environment")
        if not env_name or not self.check_environment_name(env_name):
            self.bad_request("Unknown environment: {}".format(env_name))

        return self.delete(collection, query, delete_one=False)

    ######################
    #      DB CRUD       #
    ######################

    def read(self, collection: str, query: Optional[dict] = None,
             projection: Optional[dict] = None,
             aggregate: Optional[list] = None, sort: Optional[List[Tuple]] = None,
             skip: int = 0, limit: int = 1000):
        if query is None:
            query = {}
        if not aggregate:
            aggregate = []

        collection = self.get_collection_by_name(collection)
        skip *= limit
        if aggregate:
            pipeline = [
                {"$match": query}
            ]

            if projection:
                pipeline.append({"$project": projection})
            if sort:
                pipeline.append({"$sort": sort})

            pipeline.extend(aggregate)

            if skip:
                pipeline.append({"$skip": skip})
            if limit:
                pipeline.append({"$limit": limit})

            results = collection.aggregate(pipeline)
        else:
            results = collection.find(filter=query, projection=projection, sort=sort).skip(skip).limit(limit)

        return list(results)

    def distinct(self, collection: str, field: str, query: Optional[dict] = None):
        if query is None:
            query = {}

        collection = self.get_collection_by_name(collection)
        return list(collection.distinct(key=field, filter=query))

    def write(self, document, collection="inventory"):
        try:
            return self.get_collection_by_name(collection).insert_one(document)
        except errors.DuplicateKeyError as e:
            self.conflict("The key value ({0}) already exists".
                          format(', '.join(self.get_duplicate_key_values(e.details['errmsg']))))
        except errors.WriteError as e:
            self.bad_request('Failed to create resource for {0}'.format(str(e)))

    def delete(self, collection, query, delete_one=True):
        if delete_one is True:
            return self.get_collection_by_name(collection).delete_one(query)
        else:
            return self.get_collection_by_name(collection).delete_many(query)

    ######################
    #       Utils        #
    ######################

    def check_and_convert_datetime(self, time_key, data):
        time = data.get(time_key)

        if time:
            time = time.replace(' ', '+')
            try:
                data[time_key] = parser.parse(time)
            except (ValueError, OverflowError):
                self.bad_request("{0} must follow ISO 8610 date and time format,"
                                 "YYYY-MM-DDThh:mm:ss.sss+hhmm".format(time_key))

    @staticmethod
    def replace_colon_with_dot(s):
        return s.replace(':', '.')

    @staticmethod
    def get_duplicate_key_values(err_msg):
        return ["'{0}'".format(key) for key in re.findall(r'"([^",]+)"', err_msg)]

    @staticmethod
    def get_pagination(filters):
        page_size = filters.get('page_size', 1000)
        page = filters.get('page', 0)
        return page, page_size


class ResponderWithOnDelete(ResponderBase):
    def on_delete(self, req, resp):
        filters = self.parse_query_params(req)

        filters_requirements = {
            "env_name": self.require(str, mandatory=True),
            "ids": self.require(str, validate=self.ID_LIST),
            "all": self.require(bool, convert_to_type=True),
        }

        self.validate_query_data(filters, filters_requirements)
        query = self.build_delete_query(filters)

        if self.ID in query:
            if filters.get("all") is True:
                self.bad_request("Only one of 'ids=[<objectId>,...]' or 'all=true' "
                                 "should be specified in query arguments")
        elif filters.get("all") is not True:
            self.bad_request("Either 'ids=[<objectId>,...]' or 'all=true' should be specified in query arguments")

        result = self.delete_objects(self.COLLECTION, query)
        self.set_ok_response(resp, {"count": result.deleted_count})

    def build_delete_query(self, filters):
        query = super().build_query(filters)
        if "ids" in filters:
            query[self.ID] = {"$in": self.to_object_id_list(filters["ids"])}
        return query
