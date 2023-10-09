from ebay_api.operations import EbayOperations
from ebay_api import EbayAPIClient
from constants import APPLICATION, USER, HEADER


def main():
    ebay_operations = EbayOperations(APPLICATION, USER, HEADER)
    products = ebay_operations.get_products_descriptions("iphone", 10)
    print(products)

if __name__ == "__main__":
    main()