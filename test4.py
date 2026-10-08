class Book():

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def Borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print("You have borrowed {} by {}".format(self.title,self.author))
        else:
            print("Failed to borrow a {}".format(self.author))

    def Return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print("{} by {} has been returned".format(self.title,self.author))
        else:
            print("Failed to return a {}".format(self.title))

book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

print("--- Borrowing Demonstration ---")
book1.Borrow()
book2.Borrow()

print("\n--- Returning Demonstration ---")
book1.Return_book()
book3.Borrow()