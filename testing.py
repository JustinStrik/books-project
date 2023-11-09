import unittest
from bookdictionary import *
from insertrotations import *
from display import display_tree

# root is the real one, test is the one we are checking
def check_tree(root, test_root):
    # loop through all nodes of both trees to ensure that they 
    # have the same values (red, book_id, valid)

    # inorder traversal
    if (root == null_book):
        if (test_root != null_book):
            raise AssertionError("Expected null: " + str(root.book_id) + "\nActual: " + str(test_root.book_id))
        return
    elif (test_root == null_book):
        if (root != null_book):
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



class TestInsertions(unittest.TestCase):
    def test_insertions(self):
        self.assertEqual(1, 1)

    def test_LLb1(self):
        new_tree = GatorLibrary()
        new_tree.root = make_LL_insert_tree()
        new_tree.root = LLb(new_tree, new_tree.root)

        checking_tree = make_y_root_check_tree()
        self.assert_(check_tree(checking_tree, new_tree.root)) 

    def test_LLr1(self):
        new_tree = GatorLibrary()
        new_tree.root = make_LL_insert_tree()
        new_tree.root.right.red = False

        new_tree.root = LLr(new_tree, new_tree.root)
        checking_tree = make_LL_insert_tree()
        display_tree(checking_tree)
        checking_tree.right.red = False
        checking_tree.left.red = False

        display_tree(checking_tree)
        display_tree(new_tree.root)
        
        self.assert_(check_tree(checking_tree, new_tree.root))


def make_all_black(books):
    for book in books:
        book.red = False

if __name__ == '__main__':
    unittest.main()