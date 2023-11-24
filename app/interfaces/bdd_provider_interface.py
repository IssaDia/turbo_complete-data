from abc import abstractmethod


class BDD_PROVIDER_INTERFACE():
    @abstractmethod
    def insert_description(self):
        pass
    @abstractmethod
    def insert_image(self):
        pass
