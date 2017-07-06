###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import json

from test.api.responders_test.test_data import base
from test.api.test_base import TestBase
from test.api.responders_test.test_data import clique_types
from unittest.mock import patch


class TestCliqueTypes(TestBase):

    def test_get_clique_types_list_without_env_name(self):
        self.validate_get_request(clique_types.URL,
                                  params={},
                                  expected_code=base.BAD_REQUEST_CODE)

    def test_get_clique_types_with_invalid_filter(self):
        self.validate_get_request(clique_types.URL,
                                  params={
                                      "env_name": base.ENV_NAME,
                                      "invalid": "invalid"
                                  },
                                  expected_code=base.BAD_REQUEST_CODE)

    def test_get_clique_type_with_wrong_id(self):
        self.validate_get_request(clique_types.URL,
                                  params={
                                     "env_name": base.ENV_NAME,
                                     "id": clique_types.WRONG_ID
                                  },
                                  expected_code=base.BAD_REQUEST_CODE)

    @patch(base.RESPONDER_BASE_READ)
    def test_get_clique_type_with_id(self, read):
        self.validate_get_request(clique_types.URL,
                                  params={
                                      "env_name": base.ENV_NAME,
                                      "id": clique_types.CORRECT_ID
                                  },
                                  mocks={
                                      read: clique_types.CLIQUE_TYPES_WITH_SPECIFIC_ID
                                  },
                                  expected_response=clique_types.
                                      CLIQUE_TYPES_WITH_SPECIFIC_ID[0],
                                  expected_code=base.SUCCESSFUL_CODE
                                  )

    def test_get_clique_types_list_with_wrong_focal_point_type(self):
        self.validate_get_request(clique_types.URL,
                                  params={
                                     "env_name": base.ENV_NAME,
                                     "focal_point_type": clique_types.WRONG_FOCAL_POINT_TYPE
                                  },
                                  expected_code=base.BAD_REQUEST_CODE)

    @patch(base.RESPONDER_BASE_READ)
    def test_get_clique_types_list_with_correct_focal_point_type(self, read):
        self.validate_get_request(clique_types.URL,
                                  params={
                                     "env_name": base.ENV_NAME,
                                     "focal_point_type":
                                         clique_types.CORRECT_FOCAL_POINT_POINT_TYPE
                                  },
                                  mocks={
                                     read: clique_types.
                                         CLIQUE_TYPES_WITH_SPECIFIC_FOCAL_POINT_TYPE
                                  },
                                  expected_code=base.SUCCESSFUL_CODE,
                                  expected_response=clique_types.
                                     CLIQUE_TYPES_WITH_SPECIFIC_FOCAL_POINT_TYPE_RESPONSE
                                  )

    def test_get_clique_types_list_with_wrong_link_type(self):
        self.validate_get_request(clique_types.URL,
                                  params={
                                     "env_name": base.ENV_NAME,
                                     "link_type": clique_types.WRONG_LINK_TYPE
                                  },
                                  expected_code=base.BAD_REQUEST_CODE)

    @patch(base.RESPONDER_BASE_READ)
    def test_get_clique_types_list_with_correct_link_type(self, read):
        self.validate_get_request(clique_types.URL,
                                  params={
                                     "env_name": base.ENV_NAME,
                                     "link_type": base.CORRECT_LINK_TYPE
                                  },
                                  mocks={
                                     read: clique_types.
                                        CLIQUE_TYPES_WITH_SPECIFIC_LINK_TYPE
                                  },
                                  expected_code=base.SUCCESSFUL_CODE,
                                  expected_response=clique_types.
                                     CLIQUE_TYPES_WITH_SPECIFIC_LINK_TYPE_RESPONSE
                                  )

    def test_get_clique_types_list_with_non_int_page(self):
        self.validate_get_request(clique_types.URL,
                                  params={
                                     "env_name": base.ENV_NAME,
                                     "page": base.NON_INT_PAGE
                                  },
                                  expected_code=base.BAD_REQUEST_CODE)

    @patch(base.RESPONDER_BASE_READ)
    def test_get_clique_types_list_with_int_page(self, read):
        self.validate_get_request(clique_types.URL,
                                  params={
                                     "env_name": base.ENV_NAME,
                                     "page": base.INT_PAGE
                                  },
                                  mocks={
                                     read: clique_types.CLIQUE_TYPES
                                  },
                                  expected_code=base.SUCCESSFUL_CODE,
                                  expected_response=clique_types.CLIQUE_TYPES_RESPONSE)

    def test_get_clique_types_list_with_non_int_page_size(self):
        self.validate_get_request(clique_types.URL,
                                  params={
                                     "env_name": base.ENV_NAME,
                                     "page_size": base.NON_INT_PAGESIZE
                                  },
                                  expected_code=base.BAD_REQUEST_CODE)

    @patch(base.RESPONDER_BASE_READ)
    def test_get_clique_types_list_with_int_page_size(self, read):
        self.validate_get_request(clique_types.URL,
                                  params={
                                     "env_name": base.ENV_NAME,
                                     "page_size": base.INT_PAGESIZE
                                  },
                                  mocks={
                                     read: clique_types.CLIQUE_TYPES
                                  },
                                  expected_code=base.SUCCESSFUL_CODE,
                                  expected_response=clique_types.CLIQUE_TYPES_RESPONSE)

    @patch(base.RESPONDER_BASE_CHECK_ENVIRONMENT_NAME)
    @patch(base.RESPONDER_BASE_READ)
    def test_get_clique_types_list_with_unknown_env_name(self, read, check_env_name):
        self.validate_get_request(clique_types.URL,
                                  params={
                                      "env_name": base.UNKNOWN_ENV
                                  },
                                  mocks={
                                      read: [],
                                      check_env_name: False
                                  },
                                  expected_code=base.BAD_REQUEST_CODE)

    @patch(base.RESPONDER_BASE_CHECK_ENVIRONMENT_NAME)
    @patch(base.RESPONDER_BASE_READ)
    def test_get_clique_types_list_with_env_name_and_nonexistent_link_type(self, read, check_env_name):
        self.validate_get_request(clique_types.URL,
                                  params={
                                      "env_name": base.ENV_NAME,
                                      "link_type": clique_types.NONEXISTENT_LINK_TYPE
                                  },
                                  mocks={
                                      read: [],
                                      check_env_name: True
                                  },
                                  expected_code=base.NOT_FOUND_CODE)

    @patch(base.RESPONDER_BASE_CHECK_ENVIRONMENT_NAME)
    @patch(base.RESPONDER_BASE_READ)
    def test_get_clique_type_with_unknown_env_name_and_id(self, read, check_env_name):
        self.validate_get_request(clique_types.URL,
                                  params={
                                      "env_name": base.UNKNOWN_ENV,
                                      "id": clique_types.NONEXISTENT_ID
                                  },
                                  mocks={
                                      read: [],
                                      check_env_name: False
                                  },
                                  expected_code=base.BAD_REQUEST_CODE)

    @patch(base.RESPONDER_BASE_CHECK_ENVIRONMENT_NAME)
    @patch(base.RESPONDER_BASE_READ)
    def test_get_clique_type_with_env_name_and_nonexistent_id(self, read, check_env_name):
        self.validate_get_request(clique_types.URL,
                                  params={
                                      "env_name": base.ENV_NAME,
                                      "id": clique_types.NONEXISTENT_ID
                                  },
                                  mocks={
                                      read: [],
                                      check_env_name: True
                                  },
                                  expected_code=base.NOT_FOUND_CODE)

    def test_post_clique_type_with_non_dict_clique_type(self):
        self.validate_post_request(clique_types.URL,
                                   body=json.dumps(clique_types.NON_DICT_CLIQUE_TYPE),
                                   expected_code=base.BAD_REQUEST_CODE)

    def test_post_clique_type_without_env_name(self):
        self.validate_post_request(clique_types.URL,
                                   body=json.dumps(clique_types.CLIQUE_TYPE_WITHOUT_ENVIRONMENT),
                                   expected_code=base.BAD_REQUEST_CODE)

    @patch(base.RESPONDER_BASE_CHECK_ENVIRONMENT_NAME)
    def test_post_clique_type_with_unknown_env_name(self, check_environment_name):
        self.validate_post_request(clique_types.URL,
                                   mocks={
                                       check_environment_name: False
                                   },
                                   body=json.dumps(clique_types.
                                                   CLIQUE_TYPE_WITH_UNKNOWN_ENVIRONMENT),
                                   expected_code=base.BAD_REQUEST_CODE)

    def test_post_clique_type_without_focal_point_type(self):
        self.validate_post_request(clique_types.URL,
                                   body=json.dumps(clique_types.
                                                   CLIQUE_TYPE_WITHOUT_FOCAL_POINT_TYPE),
                                   expected_code=base.BAD_REQUEST_CODE)

    def test_post_clique_type_with_wrong_focal_point_type(self):
        self.validate_post_request(clique_types.URL,
                                   body=json.dumps(clique_types.
                                                   CLIQUE_TYPE_WITH_WRONG_FOCAL_POINT_TYPE),
                                   expected_code=base.BAD_REQUEST_CODE)

    def test_post_clique_type_without_link_types(self):
        self.validate_post_request(clique_types.URL,
                                   body=json.dumps(
                                      clique_types.CLIQUE_TYPE_WITHOUT_LINK_TYPES
                                   ),
                                   expected_code=base.BAD_REQUEST_CODE)

    def test_post_clique_type_with_non_list_link_types(self):
        self.validate_post_request(clique_types.URL,
                                   body=json.dumps(clique_types.
                                                   CLIQUE_TYPE_WITH_NON_LIST_LINK_TYPES),
                                   expected_code=base.BAD_REQUEST_CODE)

    def test_post_clique_type_with_wrong_link_type(self):
        self.validate_post_request(clique_types.URL,
                                   body=json.dumps(clique_types.
                                                   CLIQUE_TYPE_WITH_WRONG_LINK_TYPE),
                                   expected_code=base.BAD_REQUEST_CODE)

    def test_post_clique_type_without_name(self):
        self.validate_post_request(clique_types.URL,
                                   body=json.dumps(clique_types.CLIQUE_TYPE_WITHOUT_NAME),
                                   expected_code=base.BAD_REQUEST_CODE)

    @patch(base.RESPONDER_BASE_CHECK_ENVIRONMENT_NAME)
    @patch(base.RESPONDER_BASE_WRITE)
    def test_post_clique_type(self, write, check_environment_name):
        self.validate_post_request(clique_types.URL,
                                   body=json.dumps(clique_types.CLIQUE_TYPE),
                                   mocks={
                                       write: None,
                                       check_environment_name: True
                                   },
                                   expected_code=base.CREATED_CODE)
