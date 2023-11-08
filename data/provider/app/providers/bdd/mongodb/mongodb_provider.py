from app.interfaces.bdd_provider_interface import BDD_PROVIDER_INTERFACE
from app.external.mongo_db_cloud_connection import MongoDB_CONNECTION
from app.providers.data.ebay.ebay_rest.ebay_rest_provider import EBAY_REST_PROVIDER
from app.use_cases.use_cases_ebay_rest import GET_DESCRIPTIONS_USE_CASE
from app.use_cases.use_cases_ebay_rest import GET_IMAGES_USE_CASE
from pymongo import errors

class MONGODB_PROVIDER(BDD_PROVIDER_INTERFACE):

    def __init__(self, client_url):
        self._mongodb_client = MongoDB_CONNECTION(client_url)
        
    def insert_description(self):
        ebay_api_client= EBAY_REST_PROVIDER()
        fetch_descriptions=GET_DESCRIPTIONS_USE_CASE(ebay_api_client)
        try:
            descriptions=fetch_descriptions.execute("iphone", 3)
            client = self._mongodb_client._client
            db = client.turbo
            collection=db.description
            for description in descriptions:
                description_dict = {
                "id": description.description_id,
                "category": description.description_category,
                "text": description.description_text,
                }
                collection.insert_one(description_dict)

        except errors.PyMongoError as e:
                print(f"Error: {e}")
        finally:
            client.close()
    def insert_image(self):
        ebay_api_client= EBAY_REST_PROVIDER()
        fetch_images=GET_IMAGES_USE_CASE(ebay_api_client)
        client = self._mongodb_client._client
        db = client.turbo
        collection=db.image
            
        try:
           keyword = "iphone"  # Replace with your desired keyword
           limit = 1  # Replace with your desired limit
           images = fetch_images.execute(keyword, limit)
           for image in images:
                image_dict = {
                "id": image.id,
                "category": image.category,
                "keyword": image.keyword,
                "url": image.url,
                "image_data": image.image_data
                }
                collection.insert_one(image_dict)
               
        except errors.PyMongoError as e:
                print(f"Error: {e}")
        finally:
            client.close()   
        pass
    
    