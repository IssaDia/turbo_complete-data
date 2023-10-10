from app.interfaces.bdd_provider_interface import BDD_PROVIDER_INTERFACE
from app.external.mongo_db_cloud_connection import MongoDB_CONNECTION


class MONGODB_PROVIDER(BDD_PROVIDER_INTERFACE):

    def __init__(self, client_url):
        self._mongodb_client = MongoDB_CONNECTION(client_url)
    def insert_description(self):
        print("working")
        pass
    def insert_image(self):
        
        pass
    
    