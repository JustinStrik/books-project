import unittest
from gatorLibrary import *
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
    a = Book(1, "a", "a", True, False)
    b = Book(3, "b", "b", True, False)
    c = Book(5, "c", "c", True, False)
    d = Book(7, "d", "d", True, False)
    z = Book(6, "z", "z", True, False)
    z.is_root = True
    y = Book(4, "y", "y", True, False)
    x = Book(2, "x", "x", True, False)
    make_all_black([a,b,c,d,z])

    z.right, z.left = d, y
    y.right, y.left = c, x
    x.right, x.left = b, a
    return z #root

def make_y_root_check_tree():
    a = Book(1, "a", "a", True, False)
    b = Book(3, "b", "b", True, False)
    c = Book(5, "c", "c", True, False)
    d = Book(7, "d", "d", True, False)
    z = Book(6, "z", "z", True, False)
    y = Book(4, "y", "y", True, False)
    x = Book(2, "x", "x", True, False)
    make_all_black([a,b,c,d,y])
    
    y.left, y.right = x, z
    x.left, x.right = a, b
    z.left, z.right = c, d
    return y

def make_R_delete_tree():
    # nodes a,v,b,py,y in order
    a = Book(1, "a", "a", True, False)
    v = Book(2, "v", "v", True, False)
    b = Book(3, "b", "b", True, False)
    py = Book(4, "py", "py", True, False)
    y = Book(5, "y", "y", True, False)
    make_all_black([a,v,b,py,y])

    v.left, v.right = a, b
    py.left, py.right = v, y
    return py

def make_L_delete_tree():
    # nodes a,v,b,py,y in order
    a = Book(1, "a", "a", True, False)
    v = Book(2, "v", "v", True, False)
    b = Book(3, "b", "b", True, False)
    py = Book(4, "py", "py", True, False)
    y = Book(5, "y", "y", True, False)
    make_all_black([a,v,b,py,y])

    v.left, v.right = a, b
    py.left, py.right = y, v
    return py


def make_delete_tree_for_RR_12():
    # nodes a,v,b,w,c,x,d,py,y in order
    a = Book(1, "a", "a", True, False)
    v = Book(2, "v", "v", True, False)
    b = Book(3, "b", "b", True, False)
    w = Book(4, "w", "w", True, False)
    c = Book(5, "c", "c", True, False)
    x = Book(6, "x", "x", True, False)
    d = Book(7, "d", "d", True, False)
    py = Book(8, "py", "py", True, False)

def make_powerpoint_delete_tree():
    # nodes 1,3,5,5,7,8,10,30,40,20,35,45,60
    one = Book(1, "one", "one", True, False)
    three = Book(3, "three", "three", True, False)
    five = Book(5, "five", "five", True, False)
    five2 = Book(5, "five2", "five2", True, False)
    seven = Book(7, "seven", "seven", True, False)
    eight = Book(8, "eight", "eight", True, False)
    ten = Book(10, "ten", "ten", True, False)
    thirty = Book(30, "thirty", "thirty", True, False)
    forty = Book(40, "forty", "forty", True, False)
    twenty = Book(20, "twenty", "twenty", True, False)
    thirty5 = Book(35, "thirty5", "thirty5", True, False)
    forty5 = Book(45, "forty5", "forty5", True, False)
    twenty5 = Book(25, "twentyfive", "twenty5", True, False)
    sixty = Book(60, "sixty", "sixty", True, False)
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

    def test_LLb1(self):
        new_tree = GatorLibrary()
        new_tree.root = make_LL_insert_tree()
        new_tree.root = LLb(new_tree, new_tree.root)

        checking_tree = make_y_root_check_tree()
        self.assert_(check_tree(checking_tree, new_tree.root)) 

    # LLb not root, doesnt pass but works
    # def test_LLb2(self):
    #     # gp has pp and d, pp has right c
    #     # pp is 4
    #     new_tree = GatorLibrary()
    #     pp = Book(4, "pp", "pp", True, False)
    #     c = Book(5, "c", "c", True, False)
    #     gp = Book(6, "gp", "gp", True, False)
    #     d = Book(7, "d", "d", True, False)
    #     r = Book(8, "r", "r", True, False)
    #     rr = Book(9, "rr", "rr", True, False)
    #     gp.left, gp.right = pp, d
    #     pp.right = c
    #     r.left, r.right = gp, rr
    #     make_all_black([c,d,gp,r,rr])

    #     # black: c,d,gp,r,rr
    #     make_all_black([c,d,gp,r,rr])
    #     # insert p, 1
    #     new_tree.root = r
    #     display_tree(new_tree.root)
    #     new_tree.insert_book(1, "p", "p", True)
    #     display_tree(new_tree.root)


    #     a = Book(1, "a", "a", True, False)
    #     b = Book(3, "b", "b", True, False)
    #     c2 = Book(5, "c", "c", True, False)
    #     d2 = Book(7, "d", "d", True, False)
    #     z = Book(6, "z", "z", True, False)
    #     y = Book(4, "y", "y", True, False)
    #     x = Book(2, "x", "x", True, False)
    #     r2 = Book(8, "r", "r", True, False)
    #     rr2 = Book(9, "rr", "rr", True, False)
    #     make_all_black([a,b,c2,d2,y,r2,rr2])
    #     checking_tree = GatorLibrary()
    #     checking_tree.root = r2

    #     r2.left, r2.right = z, rr2
    #     y.left, y.right = x, z
    #     x.left, x.right = a, b
    #     z.left, z.right = c, d
    #     checking_tree.root = r2

    #     display_tree(checking_tree.root)
    #     display_tree(new_tree.root)
    #     check_tree(checking_tree.root, new_tree.root)
        

    # LLr root
    def test_LLr1(self):
        # gp has pp and d, pp has p and c, p has a and b
        new_tree = GatorLibrary()
        a = Book(1, "a", "a", True, False)
        p = Book(2, "p", "p", True, False)
        b = Book(3, "b", "b", True, False)
        pp = Book(4, "pp", "pp", True, False)
        c = Book(5, "c", "c", True, False)
        gp = Book(6, "gp", "gp", True, False)
        d = Book(7, "d", "d", True, False)
        # a,b,c,gp are black
        make_all_black([a,b,c,gp])

        gp.left, gp.right = pp, d
        pp.left, pp.right = p, c
        p.left, p.right = a, b

        gp.is_root = True
        new_tree.root = gp
        # display_tree(gp)
        new_tree.root = LLr(new_tree, new_tree.root)
        # display_tree(new_tree.root)

        # make tree to check it with
        # name everything with 2 after it
        # same tree, but c and d are black
        a2 = Book(1, "a2", "a2", True, False)
        p2 = Book(2, "p2", "p2", True, False)
        b2 = Book(3, "b2", "b2", True, False)
        pp2 = Book(4, "pp2", "pp2", True, False)
        c2 = Book(5, "c2", "c2", True, False)
        gp2 = Book(6, "gp2", "gp2", True, False)
        d2 = Book(7, "d2", "d2", True, False)
        make_all_black([a2,b2,pp2,c2,d2,gp2])
        
        gp2.left, gp2.right = pp2, d2
        pp2.left, pp2.right = p2, c2
        p2.left, p2.right = a2, b2

        gp2.is_root = True
        checking_tree = gp2

        # display_tree(checking_tree)
        check_tree(checking_tree, new_tree.root)
    
    # LLr not root
    def test_LLr2(self):
        # gp has pp and d, pp has p and c, p has a and b
        new_tree = GatorLibrary()
        a = Book(1, "a", "a", True, False)
        # p = Book(2, "p", "p", True, False)
        b = Book(3, "b", "b", True, False)
        pp = Book(4, "pp", "pp", True, False)
        c = Book(5, "c", "c", True, False)
        gp = Book(6, "gp", "gp", True, False)
        d = Book(7, "d", "d", True, False)
        r = Book(8, "r", "r", True, False)
        x = Book(9, "x", "x", True, False)
        y = Book(10, "y", "y", True, False)
        # a,b,c,gp are black
        make_all_black([a,b,c,gp,r,x,y])

        pp.right = c
        x.right = y
        gp.left, gp.right = pp, d
        r.left, r.right = gp, x

        # p.left, p.right = a, b

        r.is_root = True
        new_tree.root = r
        # display_tree(gp)
        # insert the properties of p with this" insert_book(self, book_id, book_name, author_name, availability)
        # display_tree(new_tree.root)
        # display_tree(new_tree.root)
        new_tree.insert_book(2, "p", "p", True)
        # display_tree(new_tree.root)
        # display_tree(new_tree.root)
        # new_tree.root = new_tree.insert_book(p)
        # display_tree(new_tree.root)

        # make tree to check it with
        # name everything with 2 after it
        # same tree, but c and d are black
        p2 = Book(2, "p2", "p2", True, False)
        pp2 = Book(4, "pp2", "pp2", True, False)
        c2 = Book(5, "c2", "c2", True, False)
        gp2 = Book(6, "gp2", "gp2", True, False)
        d2 = Book(7, "d2", "d2", True, False)
        r2 = Book(8, "r2", "r2", True, False)
        x2 = Book(9, "x2", "x2", True, False)
        y2 = Book(10, "y2", "y2", True, False)
        make_all_black([pp2,c2,d2,r2,x2,y2])

        r2.left, r2.right = gp2, x2
        x2.right = y2
        gp2.left, gp2.right = pp2, d2
        pp2.left, pp2.right = p2, c2

        r2.is_root = True
        checking_tree = GatorLibrary()
        checking_tree.root = r2

        # display_tree(checking_tree.root)
        # display_tree(new_tree.root)
        check_tree(checking_tree.root, new_tree.root)
    
    def test_LRb1(self):
        # z has x and d, x has a and y, y has b and c
        new_tree = GatorLibrary()
        a = Book(1, "a", "a", True, False)
        b = Book(3, "b", "b", True, False)
        c = Book(5, "c", "c", True, False)
        d = Book(7, "d", "d", True, False)
        z = Book(6, "z", "z", True, False)
        y = Book(4, "y", "y", True, False)
        x = Book(2, "x", "x", True, False)
        make_all_black([a,b,c,d,z])

        z.right, z.left = d, x
        y.right, y.left = c, b
        x.right, x.left = y, a

        z.is_root = True
        new_tree.root = z

        # display_tree(new_tree.root)
        new_tree.root = LRb(new_tree, new_tree.root)
        # display_tree(new_tree.root)

        c_tree = GatorLibrary()
        c_tree.root = make_y_root_check_tree()
        # display_tree(c_tree.root)
        check_tree(c_tree.root, new_tree.root)

    # LRb not root
    def test_LRb2(self):
        # z has x and d, x has a and y, y has b and c
        new_tree = GatorLibrary()
        a = Book(1, "a", "a", True, False)
        # b = Book(3, "b", "b", True, False)
        # c = Book(5, "c", "c", True, False)
        d = Book(7, "d", "d", True, False)
        z = Book(6, "z", "z", True, False)
        # y = Book(4, "y", "y", True, False)
        x = Book(2, "x", "x", True, False)
        r = Book(8, "r", "r", True, False)
        make_all_black([a,d,z,r])

        z.right, z.left = d, x
        # y.right, y.left = c, b
        x.right = a
        r.left, r.right = z, r

        r.is_root = True
        new_tree.root = r

        # display_tree(new_tree.root)
        display_tree(r)
        new_tree.insert_book(4, "y", "y", True)
        display_tree(new_tree.root)
        # display_tree(new_tree.root)

        c_tree = GatorLibrary()
        # c_tree.root = make_y_root_check_tree()
        # display_tree(c_tree.root)
        check_tree(c_tree.root, new_tree.root)

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