from pymongo import errors
from bson import ObjectId


def insert_documents(collection, documents):
    try:
        collection.insert_many(documents, ordered=True, bypass_document_validation=False, session=None)
        # for document in documents:
        #     collection.insertOne(document)
        print("Documents successfully inserted")
    except errors.PyMongoError as e:
        print(f"Error: {e}")

def get_documents(collection, filter_condition=None, limit=None):
    try:
        documents = []

        # Apply the filter condition if provided
        query = {} if filter_condition is None else filter_condition

        # Limit the number of documents if limit is provided
        cursor = collection.find(query)
        if limit is not None:
            cursor = cursor.limit(limit)

        for document_dict in cursor:
            # Convert MongoDB document to your entity
            document = {
                key: str(document_dict[key]) if isinstance(document_dict[key], ObjectId) else document_dict[key]
                for key in document_dict
            }
            documents.append(document)
        return documents
    except errors.PyMongoError as e:
        print(f"Error: {e}")
        return []