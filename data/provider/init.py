from app.providers.bdd.mongodb.mongodb_provider import MONGODB_PROVIDER
from app.use_cases.use_case_mongodb import INSERT_DESCRIPTION_USE_CASE
from app.use_cases.use_case_mongodb import INSERT_IMAGE_USE_CASE

import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_URL = os.environ.get("MONGODBCLIENT")
APPLICATION = os.environ.get("APPLICATION")
USER = os.environ.get("USER")
HEADER = os.environ.get("HEADER")

def initialize_application():
    mongodb_client = MONGODB_PROVIDER(CLIENT_URL)
    
    insert_description = INSERT_DESCRIPTION_USE_CASE(mongodb_client)
    insert_description.execute()
    
    insert_image = INSERT_IMAGE_USE_CASE(mongodb_client)
    insert_image.execute()

if __name__ == "__main__":
    initialize_application()
