from ebay_rest import API, Error
from constants import APPLICATION, USER, HEADER

class EBAY_REST_CONNECTION():

    _instance = None
    _connected = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._api = API(application=APPLICATION, user=USER, header=HEADER)
            cls._instance._connected = False
            try:
                if not cls._instance._connected:
                    cls._instance._api = API(application=APPLICATION, user=USER, header=HEADER)
                    cls._instance._connected = True
                print('Connected to Ebay API')
            except Error as error:
                print(f'Error {error.number} is {error.reason} {error.detail}. \n')
        return cls._instance

