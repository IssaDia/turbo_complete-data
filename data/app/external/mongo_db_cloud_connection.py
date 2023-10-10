from pymongo import MongoClient, errors
from app.interfaces.auth_provider_interface import AuthenticationProvider
import os
from dotenv import load_dotenv

load_dotenv()

class MongoDBAuthAuthProvider(AuthenticationProvider):
   
    def authenticate(self):
        try:
            CLIENT = os.environ.get("MONGODBCLIENT")
            client = MongoClient(CLIENT)
            client.server_info()
            db = client.get_database("turbo-complete-data")
            records = db.Description
            print(records.count_documents({}))
           
        except errors.ConnectionFailure as e:
            print("Connection failed:", e)

    def sign_out(self):
        # Implement sign-out logic here
        pass