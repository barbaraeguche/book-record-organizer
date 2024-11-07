import os
from book import Book

class BookList:
    """ this is the booklist class. it is the outer class of the node class. this class has two instance variable and several methods. """
    file_path: str = 'files'

    # inner node class of booklist
    class Node:
        """ this is the inner node class for a linked list of book objects. this class has two variables, one of type book and the other of type node and several methods. """
        
        def __init__(self, book=Book(), next=None):
            """
            this is the class constructor.

            parameters:
                b: the book object to be stored in the node
                next: the next node in the list

            returns: None
            """
            self.book = book
            self.next = next

        # accessor methods
        def get_book(self) -> Book:
            return self.book
        def get_next(self) -> 'BookList.Node':
            return self.next

        # mutator methods
        def set_book(self, book) -> None:
            self.book = Book(book)
        def set_next(self, next) -> None:
            self.next = next
        
        # equals
        def __eq__(self, obj) -> bool:
            """
            this method checks if two nodes are equal in terms of class and instance variables.

            parameters:
                obj: another object
            
            returns: true if two nodes are equal, otherwise false
            """
            if not isinstance(obj, BookList.Node):
                return False
            return self.book == obj.book and object.__eq__(self.next, obj.next)
        
    def __init__(self):
        """ this constructor initializes the head of the linked list. """
        self.head: BookList.Node = None

    def add_to_start(self, book: Book) -> None:
        """
        this method adds a book object to the start of the list.

        parameters:
            book: the book object to be added to the list
        
        returns: None
        """
        temp = self.Node(book, self.head)

        if self.head is None:
            self.head = temp
            self.head.next = self.head
        else:
            self.get_last_node().next = temp
            self.head = temp

    def store_records_by_year(self, year: int) -> None:
        """
        this method finds all the book records with the year equal to the passed year value, and stores them in its year file ie `{year}`.txt.
        
        parameters:
            year: the sought year
        
        returns: None
        """
        temp = self.head
        num_of_nodes: int = self.count_nodes()
        year_found: bool = False

        if num_of_nodes == 0:
            print("-> This list is empty... There exists no such year!")
            return
        
        if os.path.exists(f"{self.file_path}/{year}.txt"):
            os.remove(f"{self.file_path}/{year}.txt") 
            
        # traverse the list to find the desired year
        for _ in range(num_of_nodes):
            if temp.get_book().get_year() == year:
                self.open_writer(f"{self.file_path}/{year}.txt", str(temp.get_book()))
                year_found = True
            temp = temp.next

        if year_found:
            print(f"-> Book records with year {year} were found and stored in the {year}.txt file.")
        else:
            print("-> No books records with such year was found.")

    def insert_before(self, isbn: str, book: Book) -> bool:
        """
        this method searches the list for the first occurrence of a node holding a book object that has an isbn equal to the passed isbn. 
        
        if such node is found, the method will insert a new node before the found node, and return true; otherwise it does nothing and returns false.
        
        parameters:
            isbn: the sought isbn
            book: the book object to be inserted into the list
        
        returns: true if a node has a book record with the passed isbn, otherwise false
        """
        temp = self.head
        num_of_nodes: int = self.count_nodes()
        last_node: BookList.Node = self.get_last_node()

        if num_of_nodes == 0:
            print("-> This list is empty... There exists no such isbn!")
            return False
        
        # check if the head has the desired isbn
        if self.head.get_book().get_isbn() == isbn:
            last_node.next = self.Node(book, self.head)
            return True
            
        # traverse the list to find the desired isbn
        while temp.next != self.head:
            if temp.next.get_book().get_isbn() == isbn:
                temp.next = self.Node(book, temp.next)
                return True
                
            temp = temp.next

        return False

    def insert_between(self, isbn1: str, isbn2: str, book: Book) -> bool:
        """
        this method searches the list for the first occurrence of two consecutive nodes holding a book object with isbn values equal to isbn1 and isbn2 respectively.
        
        if such nodes are found, the method will insert a new node in between the found nodes and return true; otherwise nothing is inserted and returns false.
        
        parameters:
            isbn1: the first sought isbn
            isbn2: the second sought isbn
            book: the book object to be inserted into the list
        
        returns: true if two consecutive nodes having book records with the passed isbn values are found, otherwise false
        """
        temp = self.head
        num_of_nodes: int = self.count_nodes()
        last_node: BookList.Node = self.get_last_node()

        if num_of_nodes < 2:
            print("-> This list is either empty or there's only one book object, therefore nothing can be inserted between...")
            return False
        
        # if the last node and head have the desired isbn values
        if last_node.get_book().get_isbn() == isbn1 and self.head.get_book().get_isbn() == isbn2:
            last_node.next = self.Node(book, self.head)
            return True
        
        # traverse the list to find the desired isbn values
        for _ in range(num_of_nodes):
            if temp.get_book().get_isbn() == isbn1 and temp.next.get_book().get_isbn() == isbn2:
                temp.next = self.Node(book, temp.next)
                return True
        
        return False

    def display_content(self) -> None:
        """
        this method displays the linked-list records.
        
        returns: None
        """
        temp = self.head
        num_of_nodes: int = self.count_nodes()

        if num_of_nodes == 0:
            print("-> This list is empty... There is nothing to display!")
            return
        
        print("------------------------------------------------------------------------")
        for _ in range(num_of_nodes):
            print(f"{temp.get_book()} ==>")
            temp = temp.next

        # confirm end of list
        if temp == self.head:
            print("===> head")

    def delete_consecutive_records(self) -> bool:
        """
        this method traverses the list, deleting all consecutive repeated nodes, each having the same book records, if any.
        
        returns: true if all consecutive repeated nodes are found and deleted, otherwise false
        """
        temp = self.head
        num_of_nodes: int = self.count_nodes()
        last_node: BookList.Node = self.get_last_node()
        is_deleted: bool = False

        if num_of_nodes < 2:
            print("-> This list is either empty or there's only one book object...")
            return False
        
        # if the last node and head have the same book record
        if last_node.get_book() == self.head.get_book():
            self.head = self.head.next
        
        # traverse the list to find consecutive repeated nodes and delete them
        for _ in range(num_of_nodes):
            if temp.get_book() == temp.next.get_book():
                while temp.get_book() == temp.next.get_book():
                    temp.next = temp.next.next
                    is_deleted = True
            
            temp = temp.next

        return is_deleted

    def extract_author_list(self, author: str) -> 'BookList':
        """
        this method searches the list for nodes holding a book object that has an author equal to the passed author. 
        
        if such nodes are found, the method will create a new singular circular list that includes only the records of that author.
        
        parameters:
            author: the sought author
        
        returns: a new circular booklist with only the book records containing the passed author
        """
        temp = self.head
        num_of_nodes: int = self.count_nodes()
        author_list = BookList()
        author_found: bool = False

        if num_of_nodes == 0:
            print("-> This list is empty... There is no author to extract!")
            return author_list
        
        for _ in range(num_of_nodes):
            if temp.get_book().get_author() == author:
                author_list.add_to_start(temp.get_book())
                author_found = True
            temp = temp.next
        
        if author_found:
            print(f"-> Contents of the newly-created author's list for {author};")
        else:
            print("-> No books record(s) with such author was found.")
        
        return author_list

    def swap_nodes(self, isbn1: str, isbn2: str) -> bool:
        """
        this method traverses the list for the occurrence of the first pair of nodes holding book objects with isbn values equal to isbn1 and isbn2 respectively. 
        
        if such nodes are found, the method swaps the nodes, and return true; if any of these isbn are not found, nothing is swapped and returns false.
        
        parameters:
            isbn1: the first sought isbn
            isbn2: the second sought isbn
        
        returns: true if two nodes having book records with the passed isbn values are found and swapped, otherwise false
        """
        temp = curr = self.head
        num_of_nodes: int = self.count_nodes()
        book1 = book2 = Book()
        swap1 = swap2 = False

        if num_of_nodes < 2:
            print("-> This list is either empty or there's only one book object, therefore nothing can be swapped...")
            return False
        
        for _ in range(num_of_nodes):
            if temp.get_book().get_isbn() == isbn1:
                book1 = temp.get_book()
                swap1 = True
                break
        for _ in range(num_of_nodes):
            if curr.get_book().get_isbn() == isbn2:
                book2 = curr.get_book()
                swap2 = True
                break
        
        if swap1 and swap2:
            temp.set_book(book2)
            curr.set_book(book1)
            return True
        
        return False

    def commit(self) -> None:
        """
        this method commits a list by storing its contents in a file called `{commit.txt}`.
        
        returns: None
        """
        file_name: str = 'commit.txt'
        temp = self.head
        num_of_nodes: int = self.count_nodes()

        if num_of_nodes == 0:
            print("-> This list is empty... There is nothing to commit!")
            return
        
        try:
            for _ in range(num_of_nodes):
                self.open_writer(f"{self.file_path}/{file_name}", str(temp.get_book()))
                temp = temp.next

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"The records of this list have been committed to `{file_name}`")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        except FileNotFoundError:
            print(f"-> '{self.file_path}/{file_name}' file not found for committing.")


## ---------------------- HELPER FUNCTIONS  ---------------------- ##
    def count_nodes(self) -> int:
        """
        this method returns the number of nodes in the book list
        
        returns: the number of nodes in the list
        """
        temp = self.head
        if temp is None:
            return 0

        count = 1
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count

    def get_last_node(self) -> Node:
        """
        this method returns the last node in the list.
        
        returns: the reference of the last node if the list is not empty, otherwise None
        """
        temp = self.head

        if temp is None:
            return None
        while temp.next != self.head:
            temp = temp.next
        return temp

    @staticmethod
    def open_writer(file: str, text: str) -> None:
        """
        this method opens the stream for all the file objects.
        
        parameters:
            file: the file to write to
            text: the text(s) to write
        
        returns: None
        """
        with open(file, 'a') as f:
            f.write(text + '\n')

    @staticmethod
    def delete_file(file: str) -> None:
        """
        this method deletes all text files used for this program.
        
        parameters:
            file: the file to delete
        
        returns: None
        """
        if os.path.exists(file):
            os.remove(file)
