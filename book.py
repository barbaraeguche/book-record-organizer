
class Book:
    """ this is the book class. it represents a book object with title, author, price, ISBN, genre, and year as attributes. """
    
    def __init__(self, title: str = "", author: str = "", price: float = 0.0, isbn: str = "", genre: str = "", year: int = 0) -> None:
        """
        this is the class constructor.

        parameters:
            title: title of the book
            author: author of the book
            price: price of the book
            isbn: isbn of the book
            genre: genre of the book
            year: publication year of the book

        returns: None
        """
        self.title = title
        self.author = author
        self.price = price
        self.isbn = isbn
        self.genre = genre
        self.year = year
    def __copy__(self) -> 'Book':
        """
        this method creates a shallow copy of the Book object.

        returns: a shallow copy of the Book object
        """
        return type(self)(self.title, self.author, self.price, self.isbn, self.genre, self.year)

    # accessor methods
    def get_title(self) -> str:
        return self.title
    def get_author(self) -> str:
        return self.author
    def get_price(self) -> float:
        return self.price
    def get_isbn(self) -> str:
        return self.isbn
    def get_genre(self) -> str:
        return self.genre
    def get_year(self) -> int:
        return self.year

    # mutator methods
    def set_title(self, title: str) -> None:
        self.title = title
    def set_author(self, author: str) -> None:
        self.author = author
    def set_price(self, price: float) -> None:
        self.price = price
    def set_isbn(self, isbn: str) -> None:
        self.isbn = isbn
    def set_genre(self, genre: str) -> None:
       self.genre = genre
    def set_year(self, year: int) -> None:
        self.year = year

    def __eq__(self, obj) -> bool:
        """
        this method checks if two book objects are equal.

        parameters:
            obj: another object
        
        returns: true if equal, otherwise false
        """
        if not isinstance(obj, Book):
            return False
        return all(x == y for x, y in zip([self.title, self.author, self.price, self.isbn, self.genre, self.year], [obj.title, obj.author, obj.price, obj.isbn, obj.genre, obj.year]))
    
    def __str__(self) -> str:
        """
        this method returns the Book object as a string.

        returns: a string representation of the book object
        """
        return f"{self.title}, {self.author}, {self.price}, {self.isbn}, {self.genre}, {self.year}"
    