from providers.bdd.mongodb.mongodb_provider import MONGODB_PROVIDER

class INSERT_DESCRIPTION_USE_CASE:
    def __init__(self, mongodb_provider : MONGODB_PROVIDER):
        self.mongodb_provider = mongodb_provider

    def execute(self, keyword, num_elements):
        self.mongodb_provider.insert_description(keyword, num_elements)

class INSERT_IMAGE_USE_CASE:
    def __init__(self, mongodb_provider : MONGODB_PROVIDER):
        self.mongodb_provider = mongodb_provider

    def execute(self):
        self.mongodb_provider.insert_image()

class GET_DESCRIPTIONS_USE_CASE:
    def __init__(self, mongodb_provider : MONGODB_PROVIDER):
        self.mongodb_provider = mongodb_provider

    def execute(self, keyword, limit):
       return self.mongodb_provider.get_descriptions(keyword, limit)
class GET_IMAGES_USE_CASE:
    def __init__(self, mongodb_provider : MONGODB_PROVIDER):
        self.mongodb_provider = mongodb_provider

    def execute(self, keyword, limit):
        self.mongodb_provider.get_description()