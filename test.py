import unittest
from bookdictionary import *
from insertrotations import *
from display import display_tree

# root is the real one, test is the one we are checking
def check_tree(root, test_root):
    # loop through all nodes of both trees to ensure that they 
    # have the same values (red, book_id, valid)

    # inorder traversal
    if (root.get_null()):
        if (not test_root.get_null()):
            raise AssertionError("Expected null: " + str(root.book_id) + "\nActual: " + str(test_root.book_id))
        return
    elif (test_root.get_null()):
        if (not root.get_null()):
            raise AssertionError("Expected: " + str(root.book_id) + "\nActual: " + str(test_root.book_id))
        return

    check_tree(root.left, test_root.left)

    # check if red-black tree is the same for both trees
    if (root.red != test_root.red):
        print("Book with ID " + str(root.book_id) + " has different red values.")
        print("Expected: " + str(test_root.red))
        raise AssertionError("Book with ID " + str(root.book_id) + " has different red values.\nExpected: " + str(test_root.red) + "\nActual: " + str(root.red))
    if (root.book_id != test_root.book_id):
        print("Book with ID " + str(root.book_id) + " has different book_id values.")
        print("Expected: " + str(test_root.book_id))
        print("Actual: " + str(root.book_id))
        raise AssertionError("Book with ID " + str(root.book_id) + " has different book_id values.\nExpected: " + str(test_root.book_id) + "\nActual: " + str(root.book_id))
    if (root.invalid != test_root.invalid):
        print("Book with ID " + str(root.book_id) + " has different invalid values.")
        print("Expected: " + str(test_root.invalid))
        raise AssertionError("Book with ID " + str(root.book_id) + " has different invalid values.\nExpected: " + str(test_root.invalid) + "\nActual: " + str(root.invalid))
    
    check_tree(root.right, test_root.right)

    return True

def make_LL_insert_tree():
    # nodes a,b,c,d with values 1,3,5,7
    a = Book(1, "a", "a", True)
    b = Book(3, "b", "b", True)
    c = Book(5, "c", "c", True)
    d = Book(7, "d", "d", True)
    z = Book(6, "z", "z", True)
    z.is_root = True
    y = Book(4, "y", "y", True)
    x = Book(2, "x", "x", True)
    make_all_black([a,b,c,d,z])

    z.right, z.left = d, y
    y.right, y.left = c, x
    x.right, x.left = b, a
    return z #root

def make_y_root_check_tree():
    a = Book(1, "a", "a", True)
    b = Book(3, "b", "b", True)
    c = Book(5, "c", "c", True)
    d = Book(7, "d", "d", True)
    z = Book(6, "z", "z", True)
    y = Book(4, "y", "y", True)
    x = Book(2, "x", "x", True)
    make_all_black([a,b,c,d,y])
    
    y.left, y.right = x, z
    x.left, x.right = a, b
    z.left, z.right = c, d
    return y

def make_R_delete_tree():
    # nodes a,v,b,py,y in order
    a = Book(1, "a", "a", True)
    v = Book(2, "v", "v", True)
    b = Book(3, "b", "b", True)
    py = Book(4, "py", "py", True)
    y = Book(5, "y", "y", True)
    make_all_black([a,v,b,py,y])

    v.left, v.right = a, b
    py.left, py.right = v, y
    return py

def make_L_delete_tree():
    # nodes a,v,b,py,y in order
    a = Book(1, "a", "a", True)
    v = Book(2, "v", "v", True)
    b = Book(3, "b", "b", True)
    py = Book(4, "py", "py", True)
    y = Book(5, "y", "y", True)
    make_all_black([a,v,b,py,y])

    v.left, v.right = a, b
    py.left, py.right = y, v
    return py


def make_delete_tree_for_RR_12():
    # nodes a,v,b,w,c,x,d,py,y in order
    a = Book(1, "a", "a", True)
    v = Book(2, "v", "v", True)
    b = Book(3, "b", "b", True)
    w = Book(4, "w", "w", True)
    c = Book(5, "c", "c", True)
    x = Book(6, "x", "x", True)
    d = Book(7, "d", "d", True)
    py = Book(8, "py", "py", True)

def make_powerpoint_delete_tree():
    # nodes 1,3,5,5,7,8,10,30,40,20,35,45,60
    one = Book(1, "one", "one", True)
    three = Book(3, "three", "three", True)
    five = Book(5, "five", "five", True)
    five2 = Book(5, "five2", "five2", True)
    seven = Book(7, "seven", "seven", True)
    eight = Book(8, "eight", "eight", True)
    ten = Book(10, "ten", "ten", True)
    thirty = Book(30, "thirty", "thirty", True)
    forty = Book(40, "forty", "forty", True)
    twenty = Book(20, "twenty", "twenty", True)
    thirty5 = Book(35, "thirty5", "thirty5", True)
    forty5 = Book(45, "forty5", "forty5", True)
    twenty5 = Book(25, "twentyfive", "twenty5", True)
    sixty = Book(60, "sixty", "sixty", True)
    # make black 3,7,8,10,40,45,20,35
    make_all_black([three, seven, eight, ten, forty, forty5, twenty, thirty5])

    ten.left, ten.right = seven, forty
    seven.left, seven.right = three, eight
    three.left, three.right = one, five
    forty.left, forty.right = thirty, forty5
    thirty.left, thirty.right = twenty, thirty5
    twenty.right = twenty5
    forty5.right = sixty
    return ten



class TestInsertions(unittest.TestCase):
    # def test_insertions(self):
    #     self.assertEqual(1, 1)

    # def test_LLb1(self):
    #     new_tree = GatorLibrary()
    #     new_tree.root = make_LL_insert_tree()
    #     new_tree.root = LLb(new_tree, new_tree.root)

    #     checking_tree = make_y_root_check_tree()
    #     self.assert_(check_tree(checking_tree, new_tree.root)) 

    # def test_LLr1(self):
    #     new_tree = GatorLibrary()
    #     new_tree.root = make_LL_insert_tree()
    #     new_tree.root.right.red = False

    #     new_tree.root = LLr(new_tree, new_tree.root)
    #     checking_tree = make_LL_insert_tree()
    #     display_tree(checking_tree)
    #     checking_tree.right.red = False
    #     checking_tree.left.red = False

    #     display_tree(checking_tree)
    #     display_tree(new_tree.root)
        
    #     self.assert_(check_tree(checking_tree, new_tree.root))

    def test_store_reds0(self):
        new_tree = GatorLibrary()
        new_tree.root = make_powerpoint_delete_tree()
        new_tree.store_colors(new_tree.root)
    # def test_del_60_from_PP(self):
    #     new_tree = GatorLibrary()
    #     new_tree.root = make_powerpoint_delete_tree()
    #     new_tree.delete_book(new_tree.root,45)
    #     # new_tree.root = new_tree.delete_book(60)
    #     display_tree(new_tree.root)

    # def del_45_from_PP(self):
    #     new_tree = GatorLibrary()
    #     new_tree.root = make_powerpoint_delete_tree()
    #     new_tree.delete_book(new_tree.root,45)
    #     # new_tree.root = new_tree.delete_book(45)
    #     display_tree(new_tree.root)

def make_all_black(books):
    for book in books:
        book.red = False

if __name__ == '__main__':
    unittest.main()