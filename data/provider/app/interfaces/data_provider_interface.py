from abc import abstractmethod


class DATA_PROVIDER_INTERFACE():

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def get_product_by_keywords(self, product_id):
        pass

    @abstractmethod
    def search_products(self, keyword, limit):
        pass

    @abstractmethod
    def fetch_descriptions(self, keyword, limit):
        pass

    @abstractmethod
    def fetch_images():
        pass
    
    @abstractmethod
    def get_images_file():
        pass
