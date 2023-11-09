import heapq
import time
# draw_tree function defined in test.py
#import test.py
from display import display_tree
from insertrotations import insert_rotate

null_book = None
# new_book = None
class Book:
    # add function variables
    
# Note*:
# - Assume that each waitlist is limited to 20.
# - While taking timestamps, ensure the precision is high enough.
# The system should support the following operations:
# 1. PrintBook(bookID): Print information about a specific book identified by its unique bookID (e.g.,
# title, author, availability status).
# Note*: If not found, Print “BookID not found in the Library”
# 2. PrintBooks(bookID1, bookID2): Print information about all books with bookIDs in the range

    def __init__(self, book_id, book_name, author_name, availability, borrowed_by=None):
        self.book_id = book_id # unique identifier
        self.book_name = book_name # string
        self.author_name = author_name # string
        self.availability = availability  # boolean
        self.borrowed_by = borrowed_by # patron_id
        self.reservation_heap = [] # priority queue - binary min heap

        # red-black tree properties
        self.red = True
        self.left = null_book
        self.right = null_book
        self.height = 0
        # self.parent = null_book # no parent!
        self.invalid = False # when return to parent, check to see if there are two red in a row
        self.is_root = False

        # for visualization, just declaring values
        self.level = 0
        self.x = 200
        self.y = 100

    def makeLeftChild(self, parent):
        parent.left = self
 
    def makeRightChild(self, parent):
        parent.right = self

    def update_coordinates(self, x, y):
        self.x = x
        self.y = y

    def change_color(self):
        self.red = not self.red
        library.color_flip_count += 1

    def add_reservation(self, patron_id, priority):
        if len(self.reservation_heap) < 20:
            timestamp = time.time()
            heapq.heappush(self.reservation_heap, (priority, timestamp, patron_id))

    def remove_reservation(self):
        if self.reservation_heap:
            heapq.heappop(self.reservation_heap)

    def get_top_reservation(self):
        if self.reservation_heap:
            return heapq.nsmallest(1, self.reservation_heap)[0]
        else:
            return None

#declare null_book
null_book = Book(-1, "null_book", "null_book", False)
null_book.red = False
book_to_insert = null_book


class GatorLibrary:
    new_book = None

    def __init__(self):
        self.root = null_book
        self.color_flip_count = 0
        pass

    def insert_book(self, book_id, book_name, author_name, availability):
        # current = self.root
        self.new_book = Book(book_id, book_name, author_name, availability)

        # nothing in tree
        if (self.root == null_book):
            self.root = self.new_book
            self.root.red = False
            self.root.is_root = True
            return

        self.root = self.insert_book_recursive(self.root)
        if (self.root.book_id == book_id):
            self.root.red = False

    def insert_book_recursive(self, current):
        if (current == null_book):
            return self.new_book
        elif (self.new_book.book_id < current.book_id):
            current.left = self.insert_book_recursive(current.left)
        elif (self.new_book.book_id > current.book_id):
            current.right = self.insert_book_recursive(current.right)

        # check if red-black tree properties are violated
        # are there two reds in a row
        if (current.red and (current.left.red or current.right.red)):
            current.invalid = True
        
        if (current.left.invalid or current.right.invalid):
            current = insert_rotate(library,current)
            current.invalid = False

        return current # self.new_book
            
    def find_book(self, book_id):
        current = self.root
        while (current != null_book):
            if book_id == current.book_id:
                return current
            elif (book_id < current.book_id):
                current = current.left
            elif (book_id > current.book_id):
                current = current.right
        print("BookID not found in library.")
        
        

    def print_book(self, book_id):
#         BookID = <Book1 ID>
# Title = "<Book1 Name>"
# Author = "<Author1 Name"
# Availability = "<Yes | No>"
# BorrowedBy = <Patron Id | None>
# Reservations = [patron1_id,patron2_id,....]
# BookID = <Book2 ID>
# Title = "<Book2 Name>"
# Author = "<Author2 Name"
# Availability = "<Yes | No>"
# BorrowedBy = <Patron Id | None>
# Reservations = [patron1_id,patron2_id,....]
        book = self.find_book(book_id)
        if book:
            print("BookID = " + str(book.book_id))
            print("Title = " + book.book_name)
            print("Author = " + book.author_name)
            print("Availability = " + str(book.availability))
            print("BorrowedBy = " + str(book.borrowed_by))
            print("Reservations = " + str(book.reservation_heap))

    # print all books in range book_id1 to book_id2
    def print_books(self, book_id1, book_id2):
        current = self.root

        # inorder traversal of graph


        pass

    def borrow_book(self, patron_id, book_id, patron_priority):
        pass

    def return_book(self, patron_id, book_id):
        pass

    def delete_book(self, book_id):
        pass

    def find_closest_book(self, target_id):
        pass

    def color_flip_count(self):
        pass

    def execute_command(self, command):
        pass
    
def get_input():
#     Input and Output Requirements:
# ● Read input from a text file where input_filename is specified as a command-line argument.
# ● All Output should be written to a text file having filename as concatenation of input_filename + “_” +
# "output_file.txt".
# (eg. inputFilename = ‘test1.txt’ , outputFilename = ‘test1_output_file.txt’)
# ● The program should terminate when the operation encountered in the input file is Quit().
# ● While Printing Reservation Heap, only print the PatronIDs as ordered in the Heap. ( Example 3)
# Input Format
# InsertBook(bookID, title, author, availability)
# PrintBook(bookID)
# PrintBooks(bookID1, bookID2)
# BorrowBook(patronID, bookID, patronPriority)
# ReturnBook(patronID, bookID)
# Quit()
    # read command from file
    input_file = open("input.txt", "r")

    # get input file name from command line
    input_file_name = sys.argv[1]

library = GatorLibrary() # only one library, so global because why not

def main():
    # make new book
    #     def __init__(self, book_id, book_name, author_name, availability, borrowed_by=None):

    if (library.root == null_book):
        print("null_book")


    # book1 = Book(1 1234, "Harry Potter", "JK Rowling", True)
    library.insert_book(1234, "Harry Potter", "JK Rowling", True)
    library.insert_book(4567, "Harry Potter 2", "JK Dobbins", True)
    library.insert_book(7890, "Harry Potter 3", "JK Rowling", True)
    # display_tree(library.root)
    library.insert_book(590, "Harry Potter 4", "JK Rowling", True)
    library.insert_book(540, "lig book", "JK Rowling", True)
    library.insert_book(595, "RL changer, B", "JK Rowling", True)
    library.insert_book(1500, "rightest", "fug", True)
    display_tree(library.root)
    library.insert_book(1300, "RlR", "fug", True)
    display_tree(library.root)

    library.print_book(1234)
    display_tree(library.root)
    pass

if __name__ == "__main__":
    main()
    

