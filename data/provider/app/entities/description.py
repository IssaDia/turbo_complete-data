class Description() :
    def __init__(self, description_id, description_category, description_text, description_keyword):
        self.description_id = description_id
        self.description_category = description_category
        self.description_text = description_text
        self.description_keyword = description_keyword

    def __str__(self):
        return f"Description ID: {self.description_id}, Category: {self.description_category}, Description: {self.description_text}, keyword : {self.description_keyword}"