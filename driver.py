import os
from book import Book
from booklist import BookList

# ---------------------------------------------------------------- #
def open_writer(file: str, text: str) -> None:
    """
    this function opens the stream for all the file objects.
        
    parameters:
        file: the file to write to
        text: the text(s) to write
        
    returns: None
    """
    with open(file, 'a') as f:
        f.write(text + '\n')

def create_book() -> Book:
    """
    this function creates a new book object.

    returns: a newly created book object
    """
    print("Give me a book object;")

    title = input("Enter a title in double quotations: ")
    author = input("Enter an author: ")
    price = float(input("Enter a price: "))
    isbn = input("Enter an isbn value: ")
    genre = input("Enter a genre: ")
    year = int(input("Enter a year: "))
    
    return Book(title, author, price, isbn, genre, year)
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    has_commit: bool = False
    error_file: str = "files/year_err.txt"
    error_list: list = []
    book = Book()
    booklist = BookList()

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                                                  ❗Welcome to Book Record Organizer❗                                                  ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    try:
        with open("books.txt", 'r') as scan:
            lines = scan.readlines()

            for line in lines:
                books = line.strip().split(',')

                book = Book(books[0], books[1], float(books[2]), books[3], books[4], int(books[5]))
                # add book objects with invalid years to the error list
                if int(books[5]) > 2023:
                    error_list.append(book)
                    continue
                
                # add valid book objects to the linkedlist
                booklist.add_to_start(book)
        
        if error_list:
            if os.path.exists(error_file):
                os.remove(error_file)
                
            try:
                os.makedirs("files", exist_ok=True)

                for incorrect_book in error_list:
                    open_writer(error_file, str(incorrect_book))
                print(f"-> `year_err.txt` file created")
            except Exception as e:
                print(f"Error writing to {error_file}: {e}")
    except FileNotFoundError:
        print(f"{error_file} not found for reading.")
    
    print("-> Here are the contents of this list;")
    booklist.display_content()

    while True:
        print("\n\nTell me what you want to do? Let's chat since this is trending now! Here are the option:")
        print("\t\t1) Give me a year # and I would extract all records of that year and store them in a file for that year;")
        print("\t\t2) Ask me to delete all consecutive  records;")
        print("\t\t3) Give me an author name and I will create a new list with the records of this author and display them;")
        print("\t\t4) Give me an ISBN number and a Book object, and I will insert Node with the book before the record with this ISBN;")
        print("\t\t5) Give me 2 ISBN numbers and a book object, and I will insert Node between them, if I find them!")
        print("\t\t6) Give me 2 ISBN numbers and I will swap them in the list for rearrangement of records; of course if they exist!")
        print("\t\t7) Tell me to COMMIT! Your command is my wish. I will commit your list to a file called Updated_Books;")
        print("\t\t8) Tell me to STOP TALKING. Remember, if you do not commit, I will not!\n")

        code = input("Enter your selection: ")

        # ------------------------------------------------------------------------------------------------------------------------------ #
        if code == "1":
            year = int(input("Enter the year you want to extract and store in its .txt file: "))
            booklist.store_records_by_year(year)
            print("-> The contents of this list remain unchanged;")
            booklist.display_content()

        # ------------------------------------------------------------------------------------------------------------------------------ #
        elif code == "2":
            if booklist.delete_consecutive_records():
                print("-> Here are the contents of the list after removing consecutive duplicates;")
            else:
                print("-> No consecutive duplicate records were found. The contents of the list remain unchanged;")
            booklist.display_content()

        # ------------------------------------------------------------------------------------------------------------------------------ #
        elif code == "3":
            author = input("Please enter the name of the author to create an extracted list: ")

            authorlist: BookList = booklist.extract_author_list(author)
            authorlist.display_content()
            
            print("\n-> The contents of the original list remain unchanged;")
            booklist.display_content()

        # ------------------------------------------------------------------------------------------------------------------------------ #
        elif code == "4":
            isbn = input("Give me an ISBN number: ")

            if booklist.insert_before(isbn, create_book()):
                print("-> Here are the contents of the list after inserting the new Book object before the record of the given ISBN;")
            else:
                print("-> No book record such ISBN was found. The contents of this list remain unchanged;")
            booklist.display_content()

        # ------------------------------------------------------------------------------------------------------------------------------ #
        elif code == "5":
            isbn1, isbn2 = input("Give me two ISBN numbers: ").split()

            if booklist.insert_between(isbn1, isbn2, create_book()):
                print("-> Here are the contents of the list after inserting the new Book object between the two consecutive book records of the given ISBNs;")
            else:
                print("-> No consecutive book records with such ISBNs were found. The contents of this list remain unchanged;")
            booklist.display_content()

        # ------------------------------------------------------------------------------------------------------------------------------ #
        elif code == "6":
            isbn1, isbn2 = input("Give me two ISBN numbers: ").split()

            if booklist.swap_nodes(isbn1, isbn2):
                print("-> Here are the contents of the list after the given ISBNs were found and swapped;")
            else:
                print("-> Either one/both of the given ISBNs were not found in any of the book records. The contents of this list remain unchanged;")
            booklist.display_content()

        # ------------------------------------------------------------------------------------------------------------------------------ #
        elif code == "7":
            print("-> Here are the records of the list being committed;")
            booklist.display_content()
            
            booklist.commit()
            has_commit = True

        # ------------------------------------------------------------------------------------------------------------------------------ #
        elif code == "8":
            if has_commit:
                print("Leaving already? Hope to see you sometime later! :)")
                break
            else:
                print("Not so fast, you didn't COMMIT. COMMIT, or else I won't STOP TALKING...")

        # ------------------------------------------------------------------------------------------------------------------------------ #
        else:
            print("Sorry that is an invalid choice. Try again.", end="")
