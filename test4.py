class Library:

    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        