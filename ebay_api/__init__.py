from ebay_rest import API, Error


class EbayAPIClient:
    def __init__(self, application : str, user : str, header : str):
        self.application = application
        self.user = user
        self.header = header
        self.api = None
    
    def connect(self):
        try:
            self.api = API(application=self.application, user=self.user, header=self.header)
        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}. \n')