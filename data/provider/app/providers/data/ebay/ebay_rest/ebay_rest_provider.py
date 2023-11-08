from ebay_rest import API, Error
import csv
import requests
import os
from app.providers.data.ebay.ebay_rest.utils import strip_html_tags
from app.interfaces.data_provider_interface import DATA_PROVIDER_INTERFACE
from app.external.ebay_rest_connection import EBAY_REST_CONNECTION
from app.entities.description import Description
from app.entities.image import Image


class EBAY_REST_PROVIDER(DATA_PROVIDER_INTERFACE):

    def __init__(self):
        self._api_client = EBAY_REST_CONNECTION()
    def fetch_product_by_id(self, product_id : str):
        try:
            product = self._api_client._api.buy_browse_get_item(product_id)
            if product:
                return product
        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}.\n')

    def fetch_products_by_keyword(self, category_name : str, limit : int):
        products_list = []
        try:
            data = self._api_client._api.buy_browse_search(q=category_name, sort='price', limit=limit)
            for record in data:
                    if 'record' not in record:
                        pass
                    else:
                        item = record['record']
                        products_list.append(item)
            return products_list
        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}.\n')
    
    def fetch_product_descriptions(self, keyword : str, limit : int):
        try:
            products_list = self.fetch_products_by_keyword(keyword, limit)
            products_ids = []
            descriptions = []
            description_id = 1
            if products_list:
                for product in products_list:
                    products_ids.append(product['item_id'])
                
                for id in products_ids:
                    item = self.fetch_product_by_id(id)
                    if item:
                        description_text = strip_html_tags(item['description'])
                        description_category = item['category_path']
                        description_keyword=keyword
                        description_obj= Description(description_id, description_category, description_text, description_keyword)
                        description_id += 1
                        descriptions.append(description_obj)
            return descriptions

        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}.\n')
    
    def transform_descriptions_to_csv(self, descriptions_list : list[str], filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'CATEGORY', 'DESCRIPTION'])
            for i, description in enumerate(descriptions_list, start=1):
                writer.writerow([i, description[1], description[0]])
    
    def get_and_export_product_descriptions(self, category_name : str, limit: int):
        try:
            descriptions = self.fetch_product_descriptions(category_name, limit)
            if descriptions:
                self.transform_descriptions_to_csv(descriptions, 'descriptions.csv')
                print(f'Description list to csv suceed!')
        except :
            print(f'Couldn\'t transform to a CSV file')
    
    def fetch_products_images_url(self, keyword : str, limit : int):
        products = self.fetch_products_by_keyword(keyword, limit)
        images_url = []
        if products:
            for product in products:
                image_url = product['image']['image_url']
                images_url.append(image_url)
        return images_url
    
    def get_images_file(self, keyword : str,limit : int,  folder_target : str):
        images_url = self.fetch_products_images_url(keyword, limit)
        image_objects = [] 
        image_id=0
        for i, image_url in enumerate(images_url):
            response = requests.get(image_url)
            if response.status_code == 200:
                image = Image(
                id=i,
                category="cat",
                keyword=keyword,
                url=image_url,
                image_data=response.content
                )
                image_id += 1
                print(f'Image {image} downloaded')
                image_objects.append(image)
            else:
                print('Failed to download image')
        return image_objects

    