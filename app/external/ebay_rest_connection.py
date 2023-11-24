from ebay_rest import API, Error
import os
from dotenv import load_dotenv

load_dotenv()
# print(os.environ['HEADER'])

APPLICATION = 'production_1'
USER = 'production_1'
HEADER = 'US'
MONGODBCLIENT="mongodb+srv://issadiapro:issadiapro@cluster0.bpolggg.mongodb.net/"



class EBAY_REST_CONNECTION():

    _instance = None
    _connected = False

    def __init__(self):
        if not self._connected:
            try:
                self.api = API(application=APPLICATION, user=USER, header=HEADER)
                print('Connected to Ebay API')
                self._connected = True
            except Error as error:
                print(f'Error {error.number} is {error.reason} {error.detail}. \n')

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connected = False
        return cls._instance
