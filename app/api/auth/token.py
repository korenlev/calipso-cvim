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
        token = {}
        token['issued_at'] = datetime.datetime.now()
        token['expires_at'] = token['issued_at'] +\
                              datetime.timedelta(seconds=Token.token_lifetime)
        token['token'] = uuid.uuid4().hex
        token['method'] = method
        return token

    @classmethod
    def validate_token(cls, token):
        error = None
        now = datetime.datetime.now()
        if now > token['expires_at']:
            error = 'Token {0} has expired'.format(token['token'])

        return error
