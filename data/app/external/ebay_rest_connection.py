from ebay_rest import API, Error
from constants import APPLICATION, USER, HEADER
import os
from dotenv import load_dotenv

load_dotenv()

class EBAY_REST_CONNECTION():

    _instance = None
    _connected = False

    APPLICATION = os.environ.get("APPLICATION")
    USER = os.environ.get("USER")
    HEADER = os.environ.get("HEADER")

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._api = API(application=APPLICATION, user=USER, header=HEADER)
            print(APPLICATION)
            cls._instance._connected = False
            try:
                if not cls._instance._connected:
                    cls._instance._api = API(application=APPLICATION, user=USER, header=HEADER)
                    cls._instance._connected = True
                print('Connected to Ebay API')
            except Error as error:
                print(f'Error {error.number} is {error.reason} {error.detail}. \n')
        return cls._instance

