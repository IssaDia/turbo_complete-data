from ebay_rest import API, Error
from ebay_api import EbayAPIClient

class EbayOperations:
    def __init__(self, application : str, user : str, header : str):
        self._api = EbayAPIClient(application, user, header)
        self._connected = False
        try:
            if not self._connected:
                self._api.connect()
                self._connected = True
            print('Connected to Ebay API')
        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}. \n')