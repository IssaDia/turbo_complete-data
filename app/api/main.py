import os, sys
sys.path.insert(0, os.path.abspath(".."))
from flask import Flask, render_template, request, jsonify
from use_cases.use_case_mongodb import GET_DESCRIPTIONS_USE_CASE
from providers.bdd.mongodb.mongodb_provider import MONGODB_PROVIDER
from use_cases.use_case_mongodb import INSERT_DESCRIPTION_USE_CASE

app = Flask(__name__)

# CLIENT_URL = os.environ.get("MONGODBCLIENT")
CLIENT_URL = "mongodb+srv://issadiapro:issadia@cluster0.bpolggg.mongodb.net/"

@app.route('/', methods=['POST'])
def home():
   
    keyword = request.form.get('keyword')
    num_elements = request.form.get('num_elements')

    if keyword and num_elements:
        num_elements = int(num_elements)
        mongodb_provider = MONGODB_PROVIDER(CLIENT_URL)
        insert_description_use_case = INSERT_DESCRIPTION_USE_CASE(mongodb_provider)
        insert_description_use_case.execute(keyword, num_elements)
        get_descriptions_use_case = GET_DESCRIPTIONS_USE_CASE(mongodb_provider)
        descriptions = get_descriptions_use_case.execute(keyword, num_elements)
        return jsonify(descriptions)
    else:
            return jsonify({'error': 'Invalid form submission'})
      

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
