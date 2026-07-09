class library:
    def __init__(self, title, author, year):
        self.title= title
        self.author= author
        self.year= year
        self.is_borrowed= False
    def getdata(self):
        number= int(input("how many books: "))
        books= []
        for i in range(number):
            print(f"\nBook {i+1}")
            title= input("title: ")
            author= input("author: ")
            year= int(input("year: "))
            book= library(title, author, year)
            books.append(book)

    def display(self):
        print("todays report: ")
        print(f"title {self.title.upper()} ")
        print(f"author: {self.author.title()}")
        print(f"year: {self.year}")
    def borrow(self):
        if self.is_borrowed:
            print("book already borrowed.")
        else:
            self.is_borrowed=True
            print("book borrowed successfully.")
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
            print("book is not borrowed.")
        else:
            print("book returned.")

l= library("", "", 0)
l.getdata()
l.display()
l.borrow()
l.return_book()