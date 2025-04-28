class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def set_details(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"

book = Book("1984", "George Orwell", 15.99)
print(book.get_details())