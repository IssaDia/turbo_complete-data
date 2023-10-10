from ebay_rest import API, Error
from constants import APPLICATION, USER, HEADER
import os
from dotenv import load_dotenv

load_dotenv()

class EBAY_REST_CONNECTION():

    _instance = None
    _connected = False


    def __new__(cls):
        if cls._instance is None:
            try:
                cls._instance = super().__new__(cls)
                cls._instance._api = API(application=APPLICATION, user=USER, header=HEADER)
                print('Connected to Ebay API')
                cls._instance._connected = False

            except Error as error:
                print(f'Error {error.number} is {error.reason} {error.detail}. \n')
        return cls._instance

