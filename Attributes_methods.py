class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    #method
    def description(self):
        return f"Book title is {self.title} and Author is {self.author}!"

book1 = Book("Infinity","Priyanka Chopra")
print(book1.description())