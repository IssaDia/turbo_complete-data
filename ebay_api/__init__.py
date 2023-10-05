from ebay_rest import API, Error


class EBAY_API:
    def __init__(self, application : str, user : str, header : str):
        self.application = application
        self.user = user
        self.header = header
    
    def connect(self):
        try:
            api = API(application=self.application, user=self.user, header=self.header)
            self.api = api
        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}. \n')