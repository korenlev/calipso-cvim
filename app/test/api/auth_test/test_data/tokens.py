URL = '/auth/tokens'

AUTH_OBJ_WITHOUT_AUTH = {

}

AUTH_OBJ_WITHOUT_METHODS = {
    'auth': {}
}

AUTH_OBJ_WITHOUT_CREDENTIALS = {
    'auth': {
        'methods': ['credentials']
    }
}

AUTH_OBJ_WITHOUT_TOKEN = {
    'auth': {
        'methods': ['token']
    }
}

AUTH_OBJ_WITH_WRONG_CREDENTIALS = {
    'auth': {
        'methods': ['credentials'],
        'credentials': {
            'username': 'wrong_user',
            'password': 'password'
        }
    }
}

AUTH_OBJ_WITH_WRONG_TOKEN = {
    'auth': {
        'methods': ['token'],
        'token': 'wrong_token'
    }
}

AUTH_OBJ_WITH_CORRECT_CREDENTIALS = {
    'auth': {
        'methods': ['credentials'],
        'credentials': {
            'username': 'wrong_user',
            'password': 'password'
        }
    }
}

AUTH_OBJ_WITH_CORRECT_TOKEN = {
    'auth': {
        'methods': ['token'],
        'token': '17dfa88789aa47f6bb8501865d905f13'
    }
}

HEADER_WITHOUT_TOKEN = {

}

HEADER_WITH_WRONG_TOKEN = {
    'X-Auth-Token': 'wrong token'
}

HEADER_WITH_CORRECT_TOKEN = {
    'X-Auth-Token': '17dfa88789aa47f6bb8501865d905f13'
}
