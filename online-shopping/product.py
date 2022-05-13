"""Implement your Product class in this file!"""
#A Product will contain a name, a description, a seller, a collection of reviews, a price, and an availability.

class Product:

    def __init__(self, name, description, price, seller):
        self.name = name
        self.description = description
        self.reviews = set()
        self.price = price
        self.__available = True

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, val):
        self.__available = val


