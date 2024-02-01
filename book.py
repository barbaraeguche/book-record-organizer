
class Book:
    """Represents a Book with title, author, price, ISBN, genre, and year."""
    def __init__(self, title: str = "", author: str = "", price: float = 0.0, isbn: str = "", genre: str = "", year: int = 0) -> None:
        """
        This is the constructor for the Book class
        :param title: title of the Book
        :param author: author of the Book
        :param price: price of the Book
        :param isbn: isbn of the Book
        :param genre: genre of the Book
        :param year: publication year of the Book
        """
        self.title = title
        self.author = author
        self.setPrice(price)
        self.setIsbn(isbn)
        self.setGenre(genre)
        self.setYear(year)
    def __copy__(self) -> Book:
        """
        This method creates a shallow copy of the Book object
        :return: shallow copy of the Book object
        """
        return type(self)(self.title, self.author, self.price, self.isbn, self.genre, self.year)

    # accessor methods
    def getTitle(self) -> str:
        return self.title
    def getAuthor(self) -> str:
        return self.author
    def getPrice(self) -> float:
        return self.price
    def getIsbn(self) -> str:
        return self.isbn
    def getGenre(self) -> str:
        return self.genre
    def getYear(self) -> int:
        return self.year

    # mutator methods
    def setTitle(self, title: str) -> None:
        self.title = title
    def setAuthor(self, author: str) -> None:
        self.author = author
    def setPrice(self, price: float) -> None:
        self.price = price
    def setIsbn(self, isbn: str) -> None:
        self.isbn = isbn
    def setGenre(self, genre: str) -> None:
       self.genre = genre
    def setYear(self, year: int) -> None:
        self.year = year

    # equals
    def __eq__(self, obj) -> bool:
        """
        This method checks if two Book objects are equal
        :param obj: another object to compare
        :return: True if equal, False otherwise
        """
        if not isinstance(obj, Book):
            return False
        return self.title == obj.title and self.author == obj.author and self.price == obj.price and self.isbn == obj.isbn \
            and self.genre == obj.genre and self.year == obj.year

    # toString
    def __str__(self) -> str:
        """
        This method returns the Book object as a string.
        :return: string representation of the Book object
        """
        return f"{self.title}, {self.author}, {self.price}, {self.isbn}, {self.genre}, {self.year}"
