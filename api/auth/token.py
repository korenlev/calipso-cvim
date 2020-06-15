###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import datetime
import uuid


class Token:
    token_lifetime = 86400
    FIELD = 'X-AUTH-TOKEN'

    @classmethod
    def set_token_lifetime(cls, lifetime):
        Token.token_lifetime = lifetime

    @classmethod
    def new_uuid_token(cls, method):
        now = datetime.datetime.utcnow()
        token = {
            'token': uuid.uuid4().hex,
            'method': method,
            'issued_at': now,
            'expires_at': now + datetime.timedelta(seconds=Token.token_lifetime),
        }
        return token

    @classmethod
    def validate_token(cls, token):
        error = None
        now = datetime.datetime.utcnow()
        if now > token['expires_at']:
            error = 'Token {0} has expired'.format(token['token'])

        return error
