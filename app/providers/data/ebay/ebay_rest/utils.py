import csv
import re
import requests
from bs4 import BeautifulSoup
from ebay_rest import API, Error
from entities.description import Description
from entities.image import Image

def strip_html_tags(html : str):
        soup = BeautifulSoup(html, 'html.parser')
        stripped_text = soup.get_text()
        text = stripped_text.splitlines()
        
        return ''.join(text).replace('  ',' ').replace('\xa0', '').replace('\t', '')

def strip_email_phone(text : str):
    return  re.sub(r'\S+@\S+|\b(?:\+\d{1,2}\s?)?\(?\d{1,4}\)?[-.\s]?\d{1,5}[-.\s]?\d{1,6}\b', '', text)

def fetch_product_by_id(self, product_id):
    try:
        product = self.api.buy_browse_get_item(product_id)
        if product:
            return product
    except Error as error:
        print(f'Error {error.number} is {error.reason} {error.detail}.\n')

def fetch_products_by_keyword(self, category_name, limit):
    products_list = []
    try:
        data = self.api.buy_browse_search(q=category_name, sort='price', limit=limit)
        for record in data:
            if 'record' not in record:
                pass
            else:
                item = record['record']
                products_list.append(item)
        return products_list
    except Error as error:
        print(f'Error {error.number} is {error.reason} {error.detail}.\n')

def fetch_product_descriptions(api_client, keyword, limit, min_feedback_score=95, min_feedback_percentage=90):
    try:
        products_list = fetch_products_by_keyword(api_client, keyword, limit)
        descriptions = []
        description_id = 1

        for product in products_list:
            print("++++++", product)
            product_id = product['item_id']
            item = fetch_product_by_id(api_client, product_id)
            if item:
                seller_feedback_score = item.get('seller', {}).get('feedback_score', 0)
                seller_feedback_percentage = float(item.get('seller', {}).get('feedback_percentage', 0))

                # Check if the seller meets the minimum feedback criteria
                if seller_feedback_score >= min_feedback_score and seller_feedback_percentage >= min_feedback_percentage:
                    description_text = strip_email_phone(strip_html_tags(item['description']))
                    description_category = item['category_path']
                    description_keyword = keyword
                    description_obj = Description(description_id, description_category, description_text,
                                                  description_keyword)
                    description_id += 1
                    descriptions.append(description_obj)

        return descriptions
    except Error as error:
        print(f'Error {error.number} is {error.reason} {error.detail}.\n')

def transform_descriptions_to_csv(descriptions_list, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'CATEGORY', 'DESCRIPTION'])
        for i, description in enumerate(descriptions_list, start=1):
            writer.writerow([i, description[1], description[0]])

def fetch_products_images_url(api_client, keyword, limit):
    products = fetch_products_by_keyword(api_client, keyword, limit)
    images_url = []
    if products:
        for product in products:
            image_url = product['image']['image_url']
            images_url.append(image_url)
    return images_url

def fetch_product_categories(api_client, keyword, limit):
    products = fetch_products_by_keyword(api_client, keyword, limit)
    categories = []
    if products:
        for product in products:
            print("--------------")
            print(product)
            category = product['categories'][0]['category_name']
            # print(category)
            categories.append(category)
    return categories

def get_images_file(api_client, keyword, limit, folder_target):
    images_url = fetch_products_images_url(api_client, keyword, limit)
    image_objects = []
    image_id = 0
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
