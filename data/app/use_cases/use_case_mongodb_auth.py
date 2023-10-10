from app.external.mongo_db_cloud_connection import MongoDBAuthAuthProvider


class MONGODB_PRODUCTS_LOGIN_CASE:
    def __init__(self, auth_provider : MongoDBAuthAuthProvider):
        self.auth_provider = auth_provider

    def execute(self):
        self.auth_provider.authenticate()