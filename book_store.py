class Book:
    def __init__(self, title, author, isbn, publication_year):

        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        # calculate age of book based on year 2025
        current_year = 2025
        return current_year - self.publication_year

    def get_summary(self):

        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


# Example usage of books
if __name__ == "__main__":
    # Create two book objects
    book1 = Book("The monk who sold his ferrari", "Robin Sharma", "9780743273565", 1997)
    book2 = Book("Magic of thinking big", "JDavid J. Schwartz", "9780735211292", 1959)

    # Print details of book1
    print("Book 1:")
    print("Title:", book1.title)
    print("Author:", book1.author)
    print("Age:", book1.get_age(), "years")
    print("Summary:", book1.get_summary())
    print()

    # Print details of book2
    print("Book 2:")
    print("Title:", book2.title)
    print("Author:", book2.author)
    print("Age:", book2.get_age(), "years")
    print("Summary:", book2.get_summary())
