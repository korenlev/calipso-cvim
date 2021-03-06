###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from typing import Optional

from api.backends import auth_backend
from api.auth.token import Token
from base.utils.inventory_mgr import InventoryMgr
from base.utils.logging.full_logger import FullLogger


class Auth:

    def __init__(self, log_file: Optional[str] = None, log_level: Optional[str] = None):
        super().__init__()
        self.inv = InventoryMgr()
        self.log = FullLogger(name="API auth", log_file=log_file, level=log_level)
        self.tokens_coll = self.inv.collections['api_tokens']

    def get_token(self, token: str) -> Optional[list]:
        tokens = None
        try:
            tokens = list(self.tokens_coll.find({'token': token}))
        except Exception as e:
            self.log.error('Failed to get token for ', str(e))

        return tokens

    def write_token(self, token: dict) -> None:
        try:
            self.tokens_coll.insert_one(token)
        except Exception as e:
            self.log.error("Failed to write new token {0} to database for {1}"
                           .format(token['token'], str(e)))
            raise ValueError('Failed to create new token')

    def delete_token(self, token):
        error = None
        try:
            self.tokens_coll.delete_one({'token': token})
        except Exception as e:
            self.log.error('Failed to delete token {0} for {1}'.
                           format(token, str(e)))
            error = 'Failed to delete token {0}'.format(token)

        return error

    def validate_credentials(self, username, pwd):
        return auth_backend.ApiAuth.authenticate_user(username, pwd)

    def validate_token(self, token) -> None:
        tokens = self.get_token(token)
        if not tokens:
            raise ValueError("Token {0} doesn't exist".format(token))
        elif len(tokens) > 1:
            self.log.error('Multiple tokens found for {0}'.format(token))
            raise ValueError("Multiple tokens found")
        else:
            t = tokens[0]
            Token.validate_token(t)
