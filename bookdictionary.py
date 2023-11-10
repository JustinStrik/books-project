import heapq
import time
from enum import Enum
# draw_tree function defined in test.py
#import test.py
from display import display_tree
from insertrotations import insert_rotate
from reservationheap import ReservationHeap, ReservationNode

null_book = None
input_file = 'input.txt' # change to sys.arg, not hard code eventually !
# make enum

Function = Enum('Function', ['PrintBook', 'PrintBooks', 'InsertBook', 'BorrowBook', 'ReturnBook', 'DeleteBook', 'FindClosestBook', 'ColorFlipCount'])

def output(text):
    # output file named input_file (variable) + _ + output_file.txt
    output_file = input_file.split('.')[0] + '_output.txt'
    with open(output_file, 'a') as f:
        f.write(text + '\n\n')
    print(text) # for debugging

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
        self.availability = availability  # 'Yes' or 'No'
        self.borrowed_by = borrowed_by # patron_id
        self.reservation_heap = ReservationHeap() # priority queue - binary min heap

        # red-black tree properties
        self.red = True
        self.left = null_book
        self.right = null_book
        self.height = 0
        # self.parent = null_book # no parent!
        self.invalid = False # when return to parent, check to see if there are two red in a row
        self.is_root = False
        self.deficient = False

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

    def add_reservation(self, patron_id, patron_priority):
        if len(self.reservation_heap.heap) < 20:
            reservation_node = ReservationNode(self, patron_id, patron_priority)
            self.reservation_heap.insert(reservation_node)
        else:
            print("The waitlist is full!")

    def remove_reservation(self):
        return self.reservation_heap.remove()

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
        output("BookID not found in library.\n")
        
        

    def print_book(self, book_id):
        book = self.find_book(book_id)
        if book:
            # output("BookID = " + str(book.book_id))
            # output("Title = " + book.book_name)
            # output("Author = " + book.author_name)
            # output("Availability = " + str(book.availability))
            # output("BorrowedBy = " + str(book.borrowed_by))
            # output("Reservations = " + str(book.reservation_heap.heap)) 
            # # combine to one output
            output("BookID = " + str(book.book_id) + "\n" +
                "Title = " + book.book_name + "\n" +
                "Author = " + book.author_name + "\n" +
                "Availability = " + str(book.availability) + "\n" +
                "BorrowedBy = " + str(book.borrowed_by) + "\n" +
                "Reservations = " + str(book.reservation_heap.heap) + "\n\n")
                   

    # overload for recursive function
    def print_found_book(self, book):
            output("BookID = " + str(book.book_id) + "\n" +
                "Title = " + book.book_name + "\n" +
                "Author = " + book.author_name + "\n" +
                "Availability = " + str(book.availability) + "\n" +
                "BorrowedBy = " + str(book.borrowed_by) + "\n" +
                "Reservations = " + str(book.reservation_heap.heap) + "\n\n")


    # print all books in range book_id1 to book_id2
    # MAKE RECURSIVE
    def print_books(self, book_id1, book_id2, current_node):
        # will only go to left subtree if the book ID larger than the lower key
        # that way, we do not traverse unnecessary nodes
        if (current_node == null_book):
            return
        if (current_node.book_id > book_id1):
            self.print_books(book_id1, book_id2, current_node.left)
        if (current_node.book_id >= book_id1 and current_node.book_id <= book_id2):
            self.print_found_book(current_node)
        if (current_node.book_id < book_id2):
            self.print_books(book_id1, book_id2, current_node.right)

    def borrow_book(self, patron_id, book_id, patron_priority):
        book = self.find_book(book_id)
        if book:
            if book.availability == 'Yes':
                book.availability = 'No'
                book.borrowed_by = patron_id
                output("Book " + str(book_id) + " Borrowed by Patron " + str(patron_id) + "\n")
            else:
                output("Book " + str(book_id) + " Reserved by Patron " + str(patron_id) + "\n")
                book.add_reservation(patron_id, patron_priority)
        

    def return_book(self, patron_id, book_id):
        book = self.find_book(book_id)
        if book:
            if book.borrowed_by == patron_id:
                book.availability = 'Yes'
                book.borrowed_by = None
                output("Book " + str(book_id) + " Returned by Patron " + str(patron_id) + "\n")
                next_person = book.remove_reservation()
                output("Book " + str(book_id) + " Allocated to Patron " + str(next_person.patron_id) + "\n")
            else:
                output("Book " + str(book_id) + " Not Borrowed by Patron " + str(patron_id) + "\n")

    def delete_book(self, book_id):
        # nothing in tree
        if (self.root == null_book):
            print("no books in the library, you cant delete anything")
            return

        self.root, successful_deletion, book_deleted = self.delete_book_recursive(self.root)
        if (self.root.book_id == book_id):
            self.root.red = False

    def delete_book_recursive(self, current):
        if (current == null_book):
            return self.new_book, True, current
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

    def find_closest_book(self, target_id):
        pass

    def color_flip_count(self):
        pass

    def execute_command(self, command):
        pass
    
def get_input():
    # read command from file
    input_file = open("input.txt", "r")

    # read each line of file
    input_commands = []
    for line in input_file:
        # split line into list of words
        function = line.split('(')[0]

        # possible functions:
        # 1. PrintBook(bookID)
        # 2. PrintBooks(bookID1, bookID2)
        # 3. InsertBook(bookID, bookName, authorName, availabilityStatus, borrowedBy, reservationHeap)
        # 4. BorrowBook(patronID, bookID, patronPriority)
        # 5. ReturnBook(patronID, bookID): 
        # 6. DeleteBook(bookID)
        # 7. FindClosestBook(targetID)
        # 8. ColorFlipCount()

        if (function == "PrintBook"):
            book_id = int(line.split('(')[1].split(')')[0])
            input_commands.append([Function.PrintBook, book_id])
        elif (function == "PrintBooks"):
            book_id1 = int(line.split('(')[1].split(',')[0])
            book_id2 = int(line.split('(')[1].split(',')[1].split(')')[0])
            input_commands.append([Function.PrintBooks, book_id1, book_id2])
        elif (function == "InsertBook"):
            book_id = int(line.split('(')[1].split(',')[0])
            book_name = line.split('(')[1].split(',')[1].split('\"')[1]
            author_name = line.split('(')[1].split(',')[2].split('\"')[1]
            availability = line.split('(')[1].split(',')[3].split(')')[0].split('\"')[1]
            input_commands.append([Function.InsertBook, book_id, book_name, author_name, availability])
        elif (function == "BorrowBook"):
            patron_id = int(line.split('(')[1].split(',')[0])
            book_id = int(line.split('(')[1].split(',')[1])
            patron_priority = int(line.split('(')[1].split(',')[2].split(')')[0])
            input_commands.append([Function.BorrowBook, patron_id, book_id, patron_priority])
        elif (function == "ReturnBook"):
            patron_id = int(line.split('(')[1].split(',')[0])
            book_id = int(line.split('(')[1].split(',')[1].split(')')[0])
            input_commands.append([Function.ReturnBook, patron_id, book_id])
        elif (function == "DeleteBook"):
            book_id = int(line.split('(')[1].split(')')[0])
            input_commands.append([Function.DeleteBook, book_id])
        elif (function == "FindClosestBook"):
            target_id = int(line.split('(')[1].split(')')[0])
            input_commands.append([Function.FindClosestBook, target_id])
        elif (function == "ColorFlipCount"):
            input_commands.append([Function.ColorFlipCount])

    return input_commands

    # get input file name from command line
    # input_file_name = sys.argv[1]

library = GatorLibrary() # only one library, so global because why not


def main():
    # make new book
    #     def __init__(self, book_id, book_name, author_name, availability, borrowed_by=None):

    if (library.root == null_book):
        print("null_book")


    input_commands = get_input()

    for command in input_commands:
        if (command[0] == Function.PrintBook):
            library.print_book(command[1])
        elif (command[0] == Function.PrintBooks):
            library.print_books(command[1], command[2], library.root)
        elif (command[0] == Function.InsertBook):
            library.insert_book(command[1], command[2], command[3], command[4])
        elif (command[0] == Function.BorrowBook):
            library.borrow_book(command[1], command[2], command[3])
        elif (command[0] == Function.ReturnBook):
            library.return_book(command[1], command[2])
        elif (command[0] == Function.DeleteBook):
            library.delete_book(command[1])
        elif (command[0] == Function.FindClosestBook):
            library.find_closest_book(command[1])
        elif (command[0] == Function.ColorFlipCount):
            library.color_flip_count()
            


    # # book1 = Book(1 1234, "Harry Potter", "JK Rowling", True)
    # library.insert_book(1234, "Harry Potter", "JK Rowling", True)
    # library.insert_book(4567, "Harry Potter 2", "JK Dobbins", True)
    # library.insert_book(7890, "Harry Potter 3", "JK Rowling", True)
    # # display_tree(library.root)
    # library.insert_book(590, "Harry Potter 4", "JK Rowling", True)
    # library.insert_book(540, "lig book", "JK Rowling", True)
    # library.insert_book(595, "RL changer, B", "JK Rowling", True)
    # library.insert_book(1500, "rightest", "fug", True)
    # display_tree(library.root)
    # library.insert_book(1300, "RlR", "fug", True)
    # display_tree(library.root)

if __name__ == "__main__":
    main()
    

