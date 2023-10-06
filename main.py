from ebay_api.operations import EbayOperations
from constants import APPLICATION, USER, HEADER


def main():
    print(APPLICATION, USER, HEADER)

    ebay_client = EbayOperations(APPLICATION, USER, HEADER)
    ebay_client.connect()

if __name__ == "__main__":
    main()