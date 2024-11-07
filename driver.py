import os
from book import Book
from booklist import BookList

# ---------------------------------------------------------------- #
def openWriter(files: str, toWrite: str) -> None:
    """
    This method opens the stream for all the file objects
    :param files: the file to write to
    :param toWrite: the text(s) to write
    :return: None
    """
    with open(files, 'a') as file:
        file.write(toWrite + '\n')

def createBook() -> Book:
    """
    This method creates a new Book object
    :return: a newly created Book object
    """
    print("Give me a Book object;")
    title = input("Enter the title in quotation marks: ")
    author = input("Enter the author: ")
    price = float(input("Enter the price: "))
    isbn = input("Enter the ISBN: ")
    genre = input("Enter the genre: ")
    year = int(input("Enter the year: "))
    return Book(title, author, price, isbn, genre, year)
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    hasCommit: bool = False
    arrLst: list = []
    book = Book()
    bkLst = BookList()

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                                   ❗Welcome to my BookList World❗This is my assignment in a Nutshell ❗                                   ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    try:
        with open("Books.txt", 'r') as scan:
            textFiles = scan.readlines()

            for file in textFiles:
                books = file.strip().split(',')

                book = Book(books[0], books[1], float(books[2]), books[3], books[4], int(books[5]))
                if int(books[5]) > 2023:  # add book objects with invalid years to the list
                    arrLst.append(book)
                    continue
                bkLst.addToStart(book)  # add valid book objects to the linkedlist
        if not len(arrLst) == 0:
            if os.path.exists("mytextfiles/YearErr.txt"):
                os.remove("mytextfiles/YearErr.txt")
            for incorrectBook in arrLst:
                openWriter("mytextfiles/YearErr.txt", str(incorrectBook))
            print("-> YearErr.txt file created")
    except FileNotFoundError:
        print("File not found for reading.")
    print("-> Here are the contents of this list;")
    bkLst.displayContent()

    while True:
        print("\n\nTell me what you want to do? Let's Chat since this is trending now! Here are the option:")
        print("\t\t1) Give me a year # and I would extract all records of that year and store them in a file for that year;")
        print("\t\t2) Ask me to delete all consecutive repeated records;")
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
            bkLst.storeRecordsByYear(year)
            print("-> The contents of this list remain unchanged;")
            bkLst.displayContent()

        # ------------------------------------------------------------------------------------------------------------------------------ #
        elif code == "2":
            if bkLst.delConsecutiveRepeatedRecords():
                print("-> Here are the contents of the list after removing consecutive duplicates;")
            else:
                print("-> No consecutive duplicate records were found. The contents of the list remain unchanged;")
            bkLst.displayContent()

        # ------------------------------------------------------------------------------------------------------------------------------ #
        elif code == "3":
            author = input("Please enter the name of the author to create an extracted list: ")

            authorList: BookList = bkLst.extractAuthList(author)
            authorList.displayContent()
            print("\n-> The contents of the original list remain unchanged;")
            bkLst.displayContent()

        # ------------------------------------------------------------------------------------------------------------------------------ #
        elif code == "4":
            isbn = input("Give me an ISBN number: ")

            if bkLst.insertBefore(isbn, createBook()):
                print("-> Here are the contents of the list after inserting the new Book object before the record of the given ISBN;")
            else:
                print("-> No book record such ISBN was found. The contents of this list remain unchanged;")
            bkLst.displayContent()

        # ------------------------------------------------------------------------------------------------------------------------------ #
        elif code == "5":
            isbn1, isbn2 = input("Give me two ISBN numbers: ").split()

            if bkLst.insertBetween(isbn1, isbn2, createBook()):
                print("-> Here are the contents of the list after inserting the new Book object between the two consecutive book records of the given ISBNs;")
            else:
                print("-> No consecutive book records with such ISBNs were found. The contents of this list remain unchanged;")
            bkLst.displayContent()

        # ------------------------------------------------------------------------------------------------------------------------------ #
        elif code == "6":
            isbn1, isbn2 = input("Give me two ISBN numbers: ").split()

            if bkLst.swap(isbn1, isbn2):
                print("-> Here are the contents of the list after the given ISBNs were found and swapped;")
            else:
                print("-> Either one/both of the given ISBNs were not found in any of the book records. The contents of this list remain unchanged;")
            bkLst.displayContent()

        # ------------------------------------------------------------------------------------------------------------------------------ #
        elif code == "7":
            print("-> Here are the records of the list being committed;")
            bkLst.displayContent()
            bkLst.commit()
            hasCommit = True

        # ------------------------------------------------------------------------------------------------------------------------------ #
        elif code == "8":
            if hasCommit:
                print("Leaving already? Hope to see you sometime later! :)")
                break
            else:
                print("Not so fast, you didn't COMMIT. COMMIT, or else I won't STOP TALKING...")

        # ------------------------------------------------------------------------------------------------------------------------------ #
        else:
            print("Sorry that is an invalid choice. Try again.", end="")
