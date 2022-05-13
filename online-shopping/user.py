"""Implement your User class in this file!"""
import product
import review


class User:

    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.reviews = set()

    def sell_product(self, name, description, price):
        return product.Product(name, description, price, self.name)

    def buy_product(self, product_name):
        product_name.available == False

    def write_review(self, text, product_name):
        product_name.reviews.add(review.Review(text, self.name, product_name))
        self.reviews.add(review.Review(text, self.name, product_name))