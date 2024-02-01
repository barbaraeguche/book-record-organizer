import os
from book import Book

class BookList:
    """
    This is the BookList class. It is the outer class of the Node class. This class has one instance variable and the following methods: default constructor, addToStart,
    storeRecordsByYear, countNodes, insertBefore, insertBetween, displayContent, reverseList, delConsecutiveRepeatedRecords, extractAuthList, swap and commit.
    """

    # inner Node class of BookList
    class Node:
        """
        This is the Node class for a linked list of Book objects, it is an inner class of the BookList class. This class has two variables, one of type Book and
        the other of type Node and the following methods: default constructor, parameterized constructor, getters and setters, and equals.
        """
        def __init__(self, b=Book(), next=None):
            """
            This is the constructor for the Node class
            :param b: the Book object to be stored in the node
            :param next: the next node in the list
            """
            self.b = b
            self.next = next

        # accessor methods
        def getB(self) -> Book:
            return self.b
        def getNext(self):
            return self.next

        # mutator methods
        def setB(self, b) -> None:
            self.b = Book(b)
        def setNext(self, next) -> None:
            self.next = next

        # equals
        def __eq__(self, obj) -> bool:
            """
            The equals method that checks if two nodes are equal in terms of class and instance variables
            :param obj: object being compared to
            :return: true if two nodes are of the same class and have equal values of all class attributes, otherwise false
            """
            if not isinstance(obj, BookList.Node):
                return False
            return self.b == obj.b and object.__eq__(self.next, obj.next)

    # default & parameterized constructors
    def __init__(self):
        """
        This is the constructor to initialize the head of the linked list
        """
        self.head: BookList.Node = None

    def addToStart(self, book: Book) -> None:
        """
        This method adds a Book object to the start of the list
        :param book: the Book object to be added to the list
        :return: None
        """
        temp = self.Node(book, self.head)

        if self.head is None:
            self.head = temp
            self.head.next = self.head
        else:
            self.getLastNode().next = temp
            self.head = temp

    def storeRecordsByYear(self, year: int) -> None:
        """
        This method finds all the book records with the year equal to the passed yr value, and stores them in its year file ie yr.txt.
        :param year: the target year being sought
        :return: None
        """
        temp = self.head
        numOfNodes: int = self.countNodes()
        yearFound: bool = False

        if numOfNodes == 0:
            print("-> This list is empty... There exists no such year!")
        else:
            if os.path.exists(f"mytextfiles/{year}.txt"):
                os.remove(f"mytextfiles/{year}.txt")
            for _ in range(numOfNodes):
                if temp.b.getYear() == year:
                    self.openWriter(f"mytextfiles/{year}.txt", str(temp.getB()))
                    yearFound = True
                temp = temp.next

        if yearFound:
            print(f"-> Book records with {year} as its year were found and stored in its {year}.txt file.")
        else:
            self.deleteFile(f"mytextfiles/{year}.txt")
            print("-> No books records with such year was found.")

    def insertBefore(self, isbn: str, book: Book) -> bool:
        """
        This method searches the list for the first occurrence of a Node holding a Book object that has an ISBN equal to the passed isbn value. If such node is found,
        the method will insert a new Node in the list (holding Book b) before that node and return true; otherwise it does nothing and returns false.
        :param isbn: the target isbn being sought
        :param book: the Book object to be inserted into the list
        :return: true if a node has a book record with an isbn equal to the passed isbn value is found, otherwise false
        """
        temp = self.head
        numOfNodes: int = self.countNodes()
        lastNode: Node = self.getLastNode()

        if numOfNodes == 0:
            print("-> This list is empty... There exists no such isbn!")
        else:
            if temp.b.getIsbn() == isbn:
                lastNode.next = self.Node(book, self.head)
                return True
            else:
                while temp.next.b.getIsbn() != isbn and temp.next != self.head:
                    temp = temp.next
                if temp.next == self.head:
                    return False
                temp.next = self.Node(book, temp.next)
                return True
        return False

    def insertBetween(self, isbn1: str, isbn2: str, book: Book) -> bool:
        """
        This method searches the list for the first occurrence of the first two consecutive nodes holding a Book object with ISBN values equal to isbn1 and isbn2
        respectively. If such node is found, the method will insert a new Node in the list (holding Book b) in between these two nodes and return true;
        otherwise nothing is inserted and returns false.
        :param isbn1: the first target isbn being sought
        :param isbn2: the second target isbn being sought
        :param book: the Book object to be inserted into the list
        :return: true if two consecutive nodes have book records with isbn values equal to the two passed isbn values respectively are found, otherwise false
        """
        temp = self.head
        numOfNodes: int = self.countNodes()
        lastNode: Node = self.getLastNode()

        if numOfNodes < 2:
            print("-> This list is either empty or there's only one book object, therefore nothing can be inserted between...")
            return False
        if lastNode.b.getIsbn() == isbn1 and temp.b.getIsbn() == isbn2:
            lastNode.next = self.Node(book, self.head)
            return True
        else:
            for _ in range(numOfNodes):
                if temp.b.getIsbn() == isbn1 and temp.next.b.getIsbn() == isbn2:
                    toAdd = self.Node(book, temp.next)
                    temp.next = toAdd
        return False

    def displayContent(self) -> None:
        """
        This method displays the records of the linked-list
        :return: None
        """
        temp = self.head
        numOfNodes: int = self.countNodes()

        if numOfNodes == 0:
            print("-> This list is empty... There is nothing to display!")
        else:
            print("------------------------------------------------------------------------")
            for _ in range(numOfNodes):
                print(f"{temp.b} ==>")
                temp = temp.next
            if temp == self.head:
                print("===> head")

    def delConsecutiveRepeatedRecords(self) -> bool:
        """
        This method searches the list, deleting all consecutive repeated nodes, each having the same Book record, if any. If a record appears
        again in the list, but at a non-consecutive node, the method will not concern itself with it.
        :return: true if all consecutive repeated nodes are found and deleted, otherwise false
        """
        temp = self.head
        numOfNodes: int = self.countNodes()
        lastNode: Node = self.getLastNode()
        deleteConsecutive: bool = False

        if numOfNodes < 2:
            print("-> This list is either empty or there's only one book object...")
            return False
        else:
            if lastNode.getB() == self.head.getB():
                self.head = self.head.next
            for _ in range(numOfNodes):
                if temp.getB() == temp.next.getB():
                    while temp.getB() == temp.next.getB():
                        temp.next = temp.next.next
                        deleteConsecutive = True
                temp = temp.next
        return deleteConsecutive

    def extractAuthList(self, author: str):
        """
        This method searches the list for occurrences of Nodes holding a Book object that has an author equal to the passed aut value. If such nodes are found,
        the method will create a new singular circular list that includes only the records of that author.
        :param author: the target author being sought
        :return: a new singular circular list that includes only the records of the passed aut value
        """
        temp = self.head
        numOfNodes: int = self.countNodes()
        authorList = BookList()
        authorFound: bool = False

        if numOfNodes == 0:
            print("-> This list is empty... There is no author to extract!")
        else:
            for _ in range(numOfNodes):
                if temp.b.getAuthor() == author:
                    authorList.addToStart(temp.getB())
                    authorFound = True
                temp = temp.next
            if authorFound:
                print(f"-> Contents of the newly-created author's list for {author};")
            else:
                print("-> No books record(s) with such author was found.")
        return authorList

    def swap(self, isbn1: str, isbn2: str) -> bool:
        """
        This method searches the list for the occurrence of the first pair of nodes holding Book objects with ISBN values equal to isbn1 and isbn2 respectively. If
        such nodes are found, the method swaps the two nodes, and return true; If any of these ISBN does not exist, nothing is swapped and returns false.
        :param isbn1: the first target isbn being sought
        :param isbn2: the second target isbn being sought
        :return: true if two nodes have book records with isbn values equal to the two passed isbn values respectively are found and swapped, otherwise false
        """
        temp = curr = self.head
        numOfNodes: int = self.countNodes()
        book1 = book2 = Book()
        swapped1 = swapped2 = False

        if numOfNodes < 2:
            print("-> This list is either empty or there's only one book object, therefore nothing can be swapped...")
            return False
        else:
            for _ in range(numOfNodes):
                if temp.b.getIsbn() == isbn1:
                    book1 = temp.getB()
                    swapped1 = True
                    break
            for _ in range(numOfNodes):
                if curr.b.getIsbn() == isbn2:
                    book2 = curr.getB()
                    swapped2 = True
                    break
            if swapped1 and swapped2:
                temp.setB(book2)
                curr.setB(book1)
                return True
            return False

    def commit(self) -> None:
        """
        This method commits the contents of the list at the time of its call by storing the contents of the list in a file called "Update_Books.txt".
        :return: None
        """
        temp = self.head
        numOfNodes: int = self.countNodes()

        if numOfNodes == 0:
            print("-> This list is empty... There is nothing to commit!")
        else:
            try:
                for _ in range(numOfNodes):
                    self.openWriter("mytextfiles/Update_Books.txt", str(temp.getB()))
                    temp = temp.next

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("The records of this list have been committed to Update_Books.txt")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            except FileNotFoundError:
                print("-> 'mytextfiles/Update_Books.txt' file not found for committing.")

# ---------------------------------------------------------------- #
    def countNodes(self) -> int:
        """
        This method returns the number of nodes in the list ie the size of the bookList
        :return: the number of nodes in the list
        """
        temp = self.head
        if temp is None:
            return 0

        count = 1
        while not temp.next == self.head:
            count += 1
            temp = temp.next
        return count

    def getLastNode(self) -> Node:
        """
        This method locates the last node in the list
        :return: the reference of the last node if the list is not empty, otherwise None
        """
        temp = self.head

        if temp is None:
            return None
        while not temp.next == self.head:
            temp = temp.next
        return temp

    @staticmethod
    def openWriter(files: str, toWrite: str) -> None:
        """
        This method opens the stream for all the file objects
        :param files: the file to write to
        :param toWrite: the text(s) to write
        :return: None
        """
        with open(files, 'a') as file:
            file.write(toWrite + '\n')

    @staticmethod
    def deleteFile(file: str) -> None:
        """
        This method deletes all the text files used in this program
        :param file: the file to delete
        :return: None
        """
        if os.path.exists(file):
            os.remove(file)
        else: pass
