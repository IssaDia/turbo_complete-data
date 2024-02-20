from interfaces.bdd_provider_interface import BDD_PROVIDER_INTERFACE
from external.mongo_db_cloud_connection import MongoDB_CONNECTION
from providers.data.ebay.ebay_rest.ebay_rest_provider import EBAY_REST_PROVIDER
from use_cases.use_cases_ebay_rest import GET_DESCRIPTIONS_USE_CASE
from providers.bdd.mongodb.utils import insert_documents, get_documents

class MONGODB_PROVIDER(BDD_PROVIDER_INTERFACE):

    def __init__(self, client_url):
        self._mongodb_client = MongoDB_CONNECTION(client_url)

    def insert_description(self, keyword, num_elements):
        ebay_api_client = EBAY_REST_PROVIDER()
        fetch_descriptions = GET_DESCRIPTIONS_USE_CASE(ebay_api_client)
        try:
            existing_descriptions = self.get_descriptions(keyword, num_elements)
            if existing_descriptions:
                return existing_descriptions
            descriptions = fetch_descriptions.execute(keyword, num_elements)


            client = self._mongodb_client._client
            db = client.turbo
            collection = db.description
            description_documents = [
                {
                    "id": description.description_id,
                    "category": description.description_category,
                    "text": description.description_text,
                    "keyword": description.description_keyword
                }
                for description in descriptions
            ]

            collection.insert_many(description_documents, ordered=True, bypass_document_validation=False, session=None)
        except Exception as e:
            print(f"An error occurred while inserting descriptions: {e}")

    def insert_image(self):
        ebay_api_client = EBAY_REST_PROVIDER()
        fetch_images = GET_IMAGES_USE_CASE(ebay_api_client)

        client = self._mongodb_client._client
        db = client.turbo
        collection = db.image

        try:
            keyword = "iphone"
            limit = 1
            images = fetch_images.execute(keyword, limit)

            image_documents = [
                {
                    "id": image.id,
                    "category": image.category,
                    "keyword": image.keyword,
                    "url": image.url,
                    "image_data": image.image_data,
                }
                for image in images
            ]

            insert_documents(collection, image_documents)
            
        finally:
            client.close()

    def get_descriptions(self, keyword, limit):
        client = self._mongodb_client._client
        db = client.turbo
        collection = db.description

        filter_condition = {'keyword': keyword}
        descriptions = get_documents(collection, filter_condition, limit)
        return descriptions

    def get_images(self):
        client = self._mongodb_client._client
        db = client.turbo
        collection = db.image
        return get_documents(collection)
