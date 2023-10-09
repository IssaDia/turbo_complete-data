from ebay_rest import API, Error

def get_product_by_id(self, product_id : str):
        try:
            product = self._api.api.buy_browse_get_item(product_id)
            if product:
                return product
        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}.\n')