import os
from pymongo.errors import OperationFailure, ConnectionFailure

from setup_initial_data import HOST, PORT, ADMIN_USER, ADMIN_DB, CALIPSO_DB, CALIPSO_USER, MongoConnector, _exit

OLD_DB_PWD = os.environ["CALIPSO_MONGO_SERVICE_OLD_PWD"]
NEW_DB_PWD = os.environ["CALIPSO_MONGO_SERVICE_NEW_PWD"]

if __name__ == "__main__":
    mongo_connector = MongoConnector(HOST, PORT)
    try:
        # Connect to admin user
        mongo_connector.connect(db=ADMIN_DB, user=ADMIN_USER, pwd=OLD_DB_PWD)

        # Change pwd for calipso user
        mongo_connector.change_password(new_pwd=NEW_DB_PWD, user=CALIPSO_USER, db=CALIPSO_DB)
        # Chande pwd for admin user
        mongo_connector.change_password(new_pwd=NEW_DB_PWD)

        # Try connecting with new password
        mongo_connector.connect(db=ADMIN_DB, user=ADMIN_USER, pwd=NEW_DB_PWD)
        mongo_connector.connect(db=CALIPSO_DB, user=CALIPSO_USER, pwd=NEW_DB_PWD)
    except ConnectionFailure:
        print("Failed to connect to mongodb")
        _exit(1)
    except OperationFailure:
        print("Failed to change user passwords")
        _exit(1)
    finally:
        mongo_connector.disconnect()

    _exit(0)
