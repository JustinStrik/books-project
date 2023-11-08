import heapq
import time

nullBook = None
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
        self.left = nullBook
        self.right = nullBook
        self.height = 0
        self.parent = nullBook



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

#declare nullBook
nullBook = Book(-1, "nullBook", "nullBook", False)

class GatorLibrary:
    def __init__(self):
        self.root = nullBook
        pass

    def insert_book(self, book_id, book_name, author_name, availability):
        pass

    def print_book(self, book_id):
        pass

    def print_books(self, book_id1, book_id2):
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

# main
def main():
    # make new book
    #     def __init__(self, book_id, book_name, author_name, availability, borrowed_by=None):

    library = GatorLibrary()
    if (library.root == nullBook):
        print("nullBook")


    book1 = Book(1, 1234, "Harry Potter", "JK Rowling", True)
    print(book1.book_id)
    pass

if __name__ == "__main__":
    main()
