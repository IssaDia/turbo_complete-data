from abc import abstractmethod


class BDD_PROVIDER_INTERFACE():
    @abstractmethod
    def insert_description(self, product_id):
        pass
    @abstractmethod
    def insert_image(self, product_id):
        pass
