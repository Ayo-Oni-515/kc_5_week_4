import math

# book class
class Book():
    """book class manages all book-related data"""
    In_memory: dict = {}

    def __init__(self, title: str, author: str, price: float,
                 stock: int):
        self.title = title
        self.author = author
        self.price = math.ceil(price)
        self.stock = stock

        # json serializable representation
        self.json = {
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "stock": self.stock
        }

        # In memory storage
        self.In_memory.update(**self.json)
