from enum import Enum
from sys import argv
# draw_tree function defined in test.py
#import test.py
from display import display_tree
from insertrotations import insert_rotate
from deleterotations import delete_rotate
from reservationheap import ReservationHeap, ReservationNode

input_file_name = '' # change to sys.arg, not hard code eventually !
closest_more_book, closest_less_book = None, None # used for closest book function
# make enum

Function = Enum('Function', ['PrintBook', 'PrintBooks', 'InsertBook', 'BorrowBook', 'ReturnBook', 'DeleteBook', 'FindClosestBook', 'ColorFlipCount', 'Quit'])

def output(text):
    # output file named input_file (variable) + _ + output_file.txt
    output_file = input_file_name.split('.')[0] + '_output.txt'
    with open(output_file, 'a') as f:
        f.write(text + '\n\n')
    # print(text) # for debugging

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

    def __init__(self, book_id, book_name, author_name, availability, null):
        self.book_id = book_id # unique identifier
        self.book_name = book_name # string
        self.author_name = author_name # string
        self.availability = availability  # 'Yes' or 'No'
        self.borrowed_by = None # patron_id
        self.reservation_heap = ReservationHeap() # priority queue - binary min heap


        # red-black tree properties
        self.red = True
        self.left, self.right = None, None
        if (null):
            self.red = False
            self.left, self.right = None, None
        else:
            self.left = make_null_book()
            self.right = make_null_book()

        self.height = 0
        # self.parent = null_book # no parent!
        self.invalid = False # when return to parent, check to see if there are two red in a row
        self.is_root = False
        self.deficient = False
        self.null = null

        # for visualization, just declaring values
        self.level = 0
        self.x = 200
        self.y = 100

    def makeLeftChild(self, parent):
        parent.left = self
 
    def makeRightChild(self, parent):
        parent.right = self

    def get_left(self):
        if (self.left == None):
            return make_null_book()
        else:
            return self.left
        
    def get_right(self):
        if (self.right == None):
            return make_null_book()
        else:
            return self.right
    
    def update_coordinates(self, x, y):
        self.x = x
        self.y = y

    def change_color(self):
        self.red = not self.red
        # library.color_flip_count += 1 # dead code, since thats not how they want us to count

    def add_reservation(self, patron_id, patron_priority):
        if len(self.reservation_heap.heap) < 20:
            reservation_node = ReservationNode(self, patron_id, patron_priority)
            self.reservation_heap.insert(reservation_node)
        else:
            print("The waitlist is full!")

    def remove_reservation(self):
        return self.reservation_heap.remove()
        
    def get_null(self):
        return self.null

#declare null_book
def make_null_book():
    null_book = Book(-1, "null_book", "null_book", False, True)
    null_book.red = False
    return null_book

def make_null_deficient_book():
    null_deficient = Book(-1, "null_book", "null_book", False, True) # added null
    null_deficient.red, null_deficient.deficient = False, True
    return null_deficient



class GatorLibrary:
    new_book = None
    colors = dict()
    color_flip_count = 0
    deleted_book = make_null_book()

    def __init__(self):
        self.root = make_null_book()
        self.root.left, self.root.right = make_null_book(), make_null_book()
        self.color_flip_count = 0
        pass

    def insert_book(self, book_id, book_name, author_name, availability):
        self.new_book = Book(book_id, book_name, author_name, availability, False)

        # nothing in tree
        if (self.root.get_null()):
            self.root = self.new_book
            self.root.red = False
            self.root.is_root = True
            return

        self.root = self.insert_book_recursive(self.root)
        if (self.root.book_id == book_id):
            self.root.red = False

    def insert_book_recursive(self, current):
        if (current.get_null()):
            return self.new_book
        elif (self.new_book.book_id < current.book_id):
            current.left = self.insert_book_recursive(current.get_left())
        elif (self.new_book.book_id > current.book_id):
            current.right = self.insert_book_recursive(current.get_right())

        # check if red-black tree properties are violated
        # are there two reds in a row
        if (current.red and (current.get_left().red or current.get_right().red)):
            current.invalid = True
        
        if (current.get_left().invalid or current.get_right().invalid):
            current = insert_rotate(library,current)
            current.invalid = False

        return current # self.new_book
            
    def find_book(self, book_id):
        current = self.root
        while (not current.get_null()):
            if book_id == current.book_id:
                return current
            elif (book_id < current.book_id):
                current = current.get_left()
            elif (book_id > current.book_id):
                current = current.get_right()
        output("Book " + str(book_id) + " not found in the library")
        
    # make surrounded by brackets and comma separated
    def make_reservation_printable(self, reservations):
        printable = "["
        for reservation in reservations:
            printable += str(reservation.patron_id)
            if reservation != reservations[-1]:
                printable += ", "

        printable += "]"
        return printable

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

            reservations = self.make_reservation_printable(book.reservation_heap.heap)
            output("BookID = " + str(book.book_id) + "\n" +
                "Title = \"" + book.book_name + "\"\n" +
                "Author = \"" + book.author_name + "\"\n" +
                "Availability = \"" + str(book.availability) + "\"\n" +
                "BorrowedBy = " + str(book.borrowed_by) + "\n" +
                "Reservations = " + reservations)
                   

    # overload for recursive function
    def print_found_book(self, book):
            reservations = self.make_reservation_printable(book.reservation_heap.heap)
            output("BookID = " + str(book.book_id) + "\n" +
                "Title = \"" + book.book_name + "\"\n" +
                "Author = \"" + book.author_name + "\"\n" +
                "Availability = \"" + str(book.availability) + "\"\n" +
                "BorrowedBy = " + str(book.borrowed_by) + "\n" +
                "Reservations = " + reservations)
            
    def print_deletion_message(self):
        msg = "Book " + str(self.deleted_book.book_id) + " is no longer available"
        if (self.deleted_book.reservation_heap.heap):
            if (len(self.deleted_book.reservation_heap.heap) == 1):
                msg +=  ". Reservation made by Patron " + str(self.deleted_book.reservation_heap.heap[0].patron_id)
                msg += " has been cancelled!"
                output(msg)
                return

            # add period because not after available, only before reservations.
            # weird
            msg += ". Reservations made by Patrons " + str(self.deleted_book.reservation_heap.heap[0].patron_id)
            for reservation in self.deleted_book.reservation_heap.heap[1:]:
                msg += ", " + str(reservation.patron_id)
            msg += " have been cancelled!"

        output(msg)


    # print all books in range book_id1 to book_id2
    # MAKE RECURSIVE
    def print_books(self, book_id1, book_id2, current_node):
        # will only go to left subtree if the book ID larger than the lower key
        # that way, we do not traverse unnecessary nodes
        if (current_node.get_null()):
            return
        if (current_node.book_id > book_id1):
            self.print_books(book_id1, book_id2, current_node.get_left())
        if (current_node.book_id >= book_id1 and current_node.book_id <= book_id2):
            self.print_found_book(current_node)
        if (current_node.book_id < book_id2):
            self.print_books(book_id1, book_id2, current_node.get_right())

    def borrow_book(self, patron_id, book_id, patron_priority):
        book = self.find_book(book_id)
        if book:
            if book.availability == 'Yes':
                book.availability = 'No'
                book.borrowed_by = patron_id
                output("Book " + str(book_id) + " Borrowed by Patron " + str(patron_id))
            else:
                output("Book " + str(book_id) + " Reserved by Patron " + str(patron_id))
                book.add_reservation(patron_id, patron_priority)
        

    def return_book(self, patron_id, book_id):
        book = self.find_book(book_id)
        if book:
            if book.borrowed_by == patron_id:
                book.availability = 'Yes'
                book.borrowed_by = None
                output("Book " + str(book_id) + " Returned by Patron " + str(patron_id))
                next_person = book.remove_reservation()
                if (next_person):
                    book.availability = 'No'
                    book.borrowed_by = next_person.patron_id
                    output("Book " + str(book_id) + " Allotted to Patron " + str(next_person.patron_id))
            else:
                output("Book " + str(book_id) + " Not Borrowed by Patron " + str(patron_id))

    def delete_book(self, current, book_id):
        # nothing in tree
        if (self.root.get_null()):
            print("no books in the library, you cant delete anything") # shouldnt run
            return
        elif (current.get_null()):
            return current

        current.left = self.delete_book(current.get_left(), book_id)
        current.right = self.delete_book(current.get_right(), book_id)

        # no need to continue, all is good here
        if (not current.get_left().deficient and not current.get_right().deficient and current.book_id != book_id):
            return current
        
        if (current.book_id == book_id):
            self.deleted_book = current # for outputting later
            # is red leaf
            if (current.get_left().get_null() and current.get_right().get_null() and current.red):
                return make_null_book() 
            # is black leaf
            elif (current.get_left().get_null() and current.get_right().get_null() and not current.red):
                
                current = make_null_deficient_book()
                # delete book recursive
                return current
            
            # is red degree 1
            elif ((current.get_left().get_null() or current.get_right().get_null()) and current.red):
                # child must be black, just combine and all good
                if (current.get_left().get_null()):
                    current = current.get_right()
                else:
                    current = current.get_left()
                return current
                
            # is black degree 1
            elif ((current.get_left().get_null() or current.get_right().get_null()) and not current.red):
                if (current.get_left().get_null()):
                    current = current.get_right() # does it change parent!!??
                else:
                    current = current.get_left()

                # if red, make black, done!
                if (current.red):
                    current.red = False
                else:
                    current.deficient = True

                return current

                # cases:
                # 1 black degree 2 node (replace with largest in left subtree)
                # what after that? - make that deficient if black
                # 2 black degree 1: its child becomes root of deficient subtree
                # if child is red, make black
                # 3 red leaf - just delete, nothing else
                # 4 black leaf, that node becomes the deficient
            # red/black degree 2
            elif (not current.get_left().get_null() and not current.get_right().get_null()):
                # find largest in left subtree
                node, parent_ofthis = current.get_left(), current
                current_color = parent_ofthis.red
                
                # display_tree(self.root)

                # node used to iterate to find largset in subtree
                while (not node.get_right().get_null()):
                    node, parent_ofthis = node.get_right(), node

                # if unchanged
                if (node == current.get_left()):
                    current.left = make_null_book()
                # is a different node, know if replace it with deficient or null
                elif (not node.red):
                    parent_ofthis.left = make_null_deficient_book()
                else:
                    parent_ofthis.left = make_null_book()
                    
                # replace current with the values of the largest in left subtree
                node.right, node.left = current.get_right(), current.left

                # if red red stay same, if black black stay same, if black replace red, make red, if red replace black, make black
                if (node.red != current_color):
                    node.red = current_color
                else:
                    node.red = not current_color

                current = node # returns to be parents child
                

        if (current.get_left().deficient or current.get_right().deficient):
            current = delete_rotate(library,current) # pass in parent

        # why this here??!!
        if (self.root.book_id == book_id):
            self.root.red = False

        return current

    def find_closest_book(self, target_id):
        if (self.root.get_null()):
            return -1
        
        global closest_less_book
        global closest_more_book
        closest_less_book = make_null_book()
        closest_more_book = make_null_book()

        self.closest = self.root
        self.find_closest_book_recursive(self.root, target_id)
        books = [closest_less_book, closest_more_book]

        # if there is a tie for lowest distance, return the book with the lowest book_id
        if (len(books) == 1):
            self.print_found_book(books[0])
        elif (len(books) == 2):
            if (abs(books[0].book_id - target_id) < abs(books[1].book_id - target_id)):
                self.print_found_book(books[0])
            elif (abs(books[0].book_id - target_id) == abs(books[1].book_id - target_id)):
                self.print_found_book(books[0])
                self.print_found_book(books[1])
            else:
                self.print_found_book(books[1])
     
    
    def find_closest_book_recursive(self, current, target_id, original=True):
        # original is to check if we are at the first call
        
        global closest_less_book
        global closest_more_book
        if (not current.get_left().get_null()):
            self.find_closest_book_recursive(current.get_left(), target_id, False)
        if (not current.get_right().get_null()):
            self.find_closest_book_recursive(current.get_right(), target_id, False)
        current_distance = abs(current.book_id - target_id)
            
        if (current.book_id >= target_id):
            if (current_distance < abs(closest_more_book.book_id - target_id) or closest_more_book.get_null()):
                closest_more_book = current
        elif (current.book_id <= target_id):
            if (current_distance < abs(closest_less_book.book_id - target_id) or closest_less_book.get_null()):
                closest_less_book = current
        

    def get_color_flip_count(self):
        output("Color Flip Count: " + str(self.color_flip_count))

    def execute_command(self, command):
        pass

    # run before an operation
    def store_colors(self, current):
        # make an array with pairs of ID and re
        if (current.get_null()):
            return
        self.colors[current.book_id] = current.red
        self.store_colors(current.get_left())
        self.store_colors(current.get_right())
    
    # run after an operation
    def count_color_changes(self, current):
        # for debugging
        changes = 0
        if current.get_null():
            return
        
        self.count_color_changes(current.get_left())
        self.count_color_changes(current.get_right())

        # if not in self.colors
        # catch key error
        try:
            self.colors[current.book_id] == None
             # do nothing, new node can't change color
        except KeyError: # newly inserted
            return

        if (current.red != self.colors[current.book_id]):
            self.color_flip_count += 1
            changes += 1

    
def get_input(filename):
    # read command from file
    input_file = open(filename, "r")

    # read each line of file
    input_commands = []
    for line in input_file:
        # split line into list of words
        function = line.split('(')[0]

        if (function == "PrintBook"):
            book_id = int(line.split('(')[1].split(')')[0])
            input_commands.append([Function.PrintBook, book_id])
        elif (function == "PrintBooks"):
            book_id1 = int(line.split('(')[1].split(',')[0])
            book_id2 = int(line.split('(')[1].split(',')[1].split(')')[0])
            input_commands.append([Function.PrintBooks, book_id1, book_id2])
        elif (function == "InsertBook"):
            book_id = int(line.split('(')[1].split(',')[0])
            book_name = line.split('\"')[1]
            author_name = line.split('\"')[3] # causes error when comma is in the name of book
            availability = line.split('\"')[5]
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
        elif (function == "Quit"):
            input_commands.append([Function.Quit])
            break
        

    return input_commands


library = GatorLibrary() # only one library, so global because why not


def main():

    # ONLY FOR DEBUG !!
    input_commands = []
    global input_file_name
    if (len(argv) < 2):
        # enter input file name
        print("Please enter the input file name")
        input_file_name = input("Enter the input file name: ")
        input_commands = get_input(input_file_name)
    else:
        input_file_name = argv[1]
        input_commands = get_input(argv[1])

    for command in input_commands:

        if (command[0] == Function.PrintBook):
            library.print_book(command[1])
        elif (command[0] == Function.PrintBooks):
            library.print_books(command[1], command[2], library.root)
        elif (command[0] == Function.InsertBook):
            library.store_colors(library.root)
            library.insert_book(command[1], command[2], command[3], command[4])
            library.count_color_changes(library.root)
        elif (command[0] == Function.BorrowBook):
            library.borrow_book(command[1], command[2], command[3])
        elif (command[0] == Function.ReturnBook):
            library.return_book(command[1], command[2])
        elif (command[0] == Function.DeleteBook):
            # print("delete " + str(command[1]))
            library.store_colors(library.root)
            library.deleted_book = make_null_book()
            # display_tree(library.root)
            library.root = library.delete_book(library.root, command[1])
            # display_tree(library.root)
            library.print_deletion_message()
            # display_tree(library.root)
            library.count_color_changes(library.root)
        elif (command[0] == Function.FindClosestBook):
            library.find_closest_book(command[1]) # includes print
        elif (command[0] == Function.ColorFlipCount):
            library.get_color_flip_count()
        elif (command[0] == Function.Quit):
            output("Program Terminated!!")
        # if (command[0] == Function.InsertBook or command[0] == Function.DeleteBook):
        #     if (command[0] == Function.InsertBook):
        #         print("insert " + str(command[1]))
        #     else:
        #         print("delete " + str(command[1]))
        #         # display_tree(library.root)
        #         print("")
        #     if command[1] == 25:
        #         print("yo")
            # display_tree(library.root)
            #display_tree(library.root)
        # if (library.find_book(6)):
        #     print("why left no exist")
        #     left_error = library.find_book(6).get_left()
        #     library.print_found_book(left_error)
        

if __name__ == "__main__":
    main()
    

