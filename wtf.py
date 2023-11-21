from gatorLibrary import *

def delete_thing(b):
    b.right = None

def main():
    # make a tree of books
    # craete int, and strings for vars
    # b1 = Book(1, "book1", "author1", True, False)
    # b2 = Book(2, "book2", "author2", True, False)
    # b3 = Book(3, "book3", "author3", True, False)
    # b4 = Book(4, "book4", "author4", True, False)
    # b5 = Book(5, "book5", "author5", True, False)
    # b1.left, b1.right = b2, b3
    # b2.left, b2.right = b4, b5
    # delete_thing(b1)
    # print(b1.right.book_id)
    t = dict()
    t[2] = 'huh'
    t.pop(2)
    t.pop(2)
    return 0


main()