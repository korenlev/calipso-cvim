# url
URL = "/messages"

MESSAGES = [{
     "level": "info",
     "environment": "Mirantis-Liberty",
     "id": "3c64fe31-ca3b-49a3-b5d3-c485d7a452e7",
     "source_system": "OpenStack"
    },
    {
    "level": "info",
    "environment": "Mirantis-Liberty",
    "id": "c7071ec0-04db-4820-92ff-3ed2b916738f",
    "source_system": "OpenStack"
    },
]

NONEXISTENT_MESSAGE_ID = "80b5e074-0f1a-4b67-810c-fa9c92d41a9f"
MESSAGE_ID = "80b5e074-0f1a-4b67-810c-fa9c92d41a98"

RELATED_OBJECT = "instance"
NONEXISTENT_RELATED_OBJECT = "nonexistent-instance"

MESSAGES_RESPONSE = {
    "messages": MESSAGES
}
