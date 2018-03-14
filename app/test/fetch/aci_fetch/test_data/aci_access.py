ACI_CONFIG = {
    "pwd": "password",
    "host": "10.0.0.1",
    "name": "ACI",
    "user": "admin"
}

EMPTY_RESPONSE = {
    "totalCount": "0",
    "imdata": []
}

LOGIN_RESPONSE = {
    "totalCount": "1",
    "imdata": [
        {
            "aaaLogin": {
                "attributes": {
                    "token": "gewAAAAAAAAAAAAAAAAAAIEJFTLzdu3de4T7g+WWa+NHyTZVOCq7CfzMn7YnpquRXFw63JE9GlrxqPJID71EHF0Vh12qRCp+j8mFlfIVH5UcXRi7nmH2trBdNYKtbdgTKupz0BfIFou+7sYpfDwWNxj/ZkZj9qBDsd8g0n6mR0OzQrj8twQs/sTAeblwHVQFQJsw4WQLTAfbiXH8mnHCIg==",
                    "urlToken": "d398a0a0642411a6a2c8c21d365e077074a88ba659cb2d6bade3c0a852262fd6",
                },
            }
        }
    ]
}

VALID_COOKIE_TOKEN = {
    'APIC-Cookie': LOGIN_RESPONSE['imdata'][0]['aaaLogin']['attributes']['token']
}
