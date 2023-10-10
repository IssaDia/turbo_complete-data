from app.external.ebay_rest_connection import EBAY_REST_CONNECTION
from app.use_cases.use_cases_ebay_rest import GET_PRODUCTS_DESCRIPTIONS_USE_CASE
from app.providers.data.ebay.ebay_rest.ebay_rest_provider import EBAY_REST_PROVIDER

def main():
    api_client = EBAY_REST_CONNECTION()
    api_service = EBAY_REST_PROVIDER(api_client)
    get_products_by_description_use_case = GET_PRODUCTS_DESCRIPTIONS_USE_CASE(api_service)
    products_by_description = get_products_by_description_use_case.execute("renault", 1)
   

if __name__ == "__main__":
    main()