URL = "/cliques"

WRONG_CLIQUE_ID = "58a2406e6a283a8bee15d43"
CORRECT_CLIQUE_ID = "58a2406e6a283a8bee15d43f"
NONEXISTENT_CLIQUE_ID = "58a2406e6a283a8bee15d43e"

WRONG_FOCAL_POINT = "58a2406e6a283a8bee15d43"
CORRECT_FOCAL_POINT = "58a2406e6a283a8bee15d43f"

WRONG_LINK_ID = "58a2406e6a283a8bee15d43"
CORRECT_LINK_ID = "58a2406e6a283a8bee15d43f"
NONEXISTENT_LINK_ID = "58a2406e6a283a8bee15d43e"

WRONG_FOCAL_POINT_TYPE = "wrong-object-type"
FOCAL_POINT_TYPE = "vnic"

# response
CLIQUES = [{
    "link_types": [
        "instance-vnic",
        "vservice-vnic",
        "vnic-vconnector"
    ],
    "environment": "Mirantis-Liberty",
    "focal_point_type": "vnic",
    "id": "576c119a3f4173144c7a75c5"
 },
    {
    "link_types": [
        "vnic-vconnector",
        "vconnector-vedge"
    ],
    "environment": "Mirantis-Liberty",
    "focal_point_type": "vconnector",
    "id": "576c119a3f4173144c7a75c6"
}
]

CLIQUES_RESPONSE = {
    "cliques": CLIQUES
}
