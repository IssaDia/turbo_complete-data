from app.providers.bdd.mongodb.mongodb_provider import MONGODB_PROVIDER

class INSERT_DESCRIPTION_USE_CASE:
    def __init__(self, mongodb_provider : MONGODB_PROVIDER):
        self.mongodb_provider = mongodb_provider

    def execute(self):
        self.mongodb_provider.insert_description()