def delete_rotate(node):
    left = node.get_left()
    right = node.get_right()
    
    # series of if-else statements to determine which rotation to do
    if (right.deficient):
        if (left.red):
            # RRn
            w_red_children = 0
            w = left.get_right()

            if (w.get_left().red):
                w_red_children += 1
            if (w.get_right().red):
                w_red_children += 1

            if (w_red_children == 0):
                node = Rr0(node)
            elif (w_red_children == 1):
                if (w.get_left().red):
                    node = Rr1_case1(node)
                else: # right is red
                    node = Rr1_case2(node)
            else: # both children are red
                node = Rr2(node)
        else: # left is black
            v = left
            v_red_children = 0

            if (v.get_left().red):
                v_red_children += 1
            if (v.get_right().red):
                v_red_children += 1

            if (v_red_children == 0):
                if (not node.red):
                    node = Rb0_case1(node)
                    node.deficient = True # already done in function
                else:
                    node = Rb0_case2(node)
            elif (v_red_children == 1):
                if (v.get_left().red):
                    node = Rb1_case1(node)
                else:
                    node = Rb1_case2(node)
            elif (v_red_children == 2):
                node = Rb2(node)
    else: # right subtree is not deficient, left must be (only reason this function is called)
        if (right.red):
            # RLn
            w_red_children = 0
            w = right.left

            if (w.get_left().red):
                w_red_children += 1
            if (w.get_right().red):
                w_red_children += 1

            if (w_red_children == 0):
                node = Lr0(node)
            elif (w_red_children == 1):
                if (w.get_left().red):
                    node = Lr1_case1(node)
                else:
                    node = Lr1_case2(node)
            else: # both children are red
                node = Lr2(node)
        else: # right is black
            v = right
            v_red_children = 0
        
            if (v.get_left().red):
                v_red_children += 1
            if (v.get_right().red):
                v_red_children += 1

            if (v_red_children == 0):
                if (not node.red):
                    node = Lb0_case1(node)
                    node.deficient = True
                else:
                    node = Lb0_case2(node)
            elif (v_red_children == 1):
                if (v.get_right().red):
                    node = Lb1_case1(node)
                else:
                    node = Lb1_case2(node)
            elif (v_red_children == 2):
                node = Lb2(node)



    left.deficient = False
    right.deficient = False
    return node

# denoted by Xcn
# y is right child of py => X = R.
# Pointer to v is black => c = b.
# v has 1 red child => n = 1.

# py is black
def Rb0_case1(py):
    py.left.change_color()
    py.right.deficient = False # right subtree isnt deficient
    py.deficient = True # now, py is deficient
    return py

# py is red
def Rb0_case2(py):
    py.right.change_color()
    py.change_color()
    py.right.deficient = False # right subtree isnt deficient
    # no change to py deficiency
    return py

# left child of v is red
def Rb1_case1(py):
    v = py.get_left()

    # v.red = py.red
    if (v.red != py.red): # change v to color of py
        v.change_color()

    if py.red:
        py.change_color() # only change color if red, it should end black

    py.left = v.get_right()
    v.right = py

    v.left.change_color() # no longer red

    py.right.deficient = False # right subtree isnt deficient
    return v

# right child of v is red
def Rb1_case2(py):
    # lr rotation
    v = py.get_left()
    #v.red = py.red
    if (v.red != py.red):
        v.change_color()

    w = py.get_left().get_right()
    w.change_color()

    # reassign w's children
    v.right = w.get_left()
    py.left = w.get_right()
    
    # make w root of subtree
    w.left = v
    w.right = py

    py.right.deficient = False 
    return w

def Rb2(py):
    # lr rotation
    v = py.get_left()
    w = py.get_left().get_right()
    if (py.red != w.red): # change w to color of py
        w.change_color()


    # py.red = False
    if (py.red):
        py.change_color()

    py.right.deficient = False 

    # reassign w's children
    v.right = w.get_left()
    py.left = w.get_right()
    
    # make w root of subtree
    w.left = v
    w.right = py

    return w

# Rrn where n is the number of red children of v's right child w
def Rr0(py):
    # LL rotation
    v = py.get_left()
    v.change_color()

    py.left = v.get_right()
    py.left.change_color()
    v.right = py

    py.right.deficient = False
    return v

# left node of w is red
def Rr1_case1(py):
    # LR rotation
    v = py.get_left()
    w = py.get_left().get_right()

    # reassign w's children
    v.right = w.get_left()
    py.left = w.get_right()

    # make w root of subtree
    w.left = v
    w.right = py

    py.right.deficient = False
    return w

# right node of w is red
def Rr1_case2(py):
    # rotation
    v = py.get_left()
    w = py.get_left().get_right()
    x = w.get_right() # the red node

    # reassign w's children
    w.right = x.get_left()
    py.left = x.get_right()

    # make w root of subtree
    x.left = v
    x.right = py

    py.right.deficient = False
    return w

def Rr2(py):
    # LR rotation
    v = py.get_left()
    w = py.get_left().get_right()
    x = w.get_right() # the red node

    # reassign w's children
    w.right = x.get_left()
    py.left = x.get_right()

    # make w root of subtree
    x.left = v
    x.right = py

    x.change_color() # now black and root of subtree
    py.right.deficient = False
    return w

# py is black
def Lb0_case1(py):
    py.right.change_color()
    py.left.deficient = False # left subtree isnt deficient
    py.deficient = True # now, py is deficient
    return py

# py is red
def Lb0_case2(py):
    py.left.change_color()
    py.change_color()
    py.left.deficient = False # left subtree isnt deficient
    # no change to py deficiency
    return py

# right child of v is red
def Lb1_case1(py):
    v = py.get_right()

    #v.red = py.red
    if (v.red != py.red): # change v to color of py
        v.change_color()

    if py.red:
        py.left.change_color() # only change color if red

    py.right = v.get_left()
    v.left = py

    v.right.change_color() # no longer red

    py.left.deficient = False # left subtree isnt deficient
    return v

# left child of v is red
def Lb1_case2(py):
    # lr rotation
    v = py.get_right()
    # v.red = py.red
    if (v.red != py.red):
        v.change_color()

    w = py.get_right().get_left()
    w.change_color()

    # reassign w's children
    v.left = w.get_right()
    py.right = w.get_left()
    
    # make w root of subtree
    w.right = v
    w.left = py

    py.left.deficient = False 
    return w

def Lb2(py):

    # lr rotation
    v = py.get_right()
    w = py.get_right().get_left()

    if (py.red != w.red): 
        w.change_color() # now black
    py.left.deficient = False 

    # py.red = False
    if (py.red):
        py.change_color()

    # reassign w's children
    v.left = w.get_right()
    py.right = w.get_left()
    
    # make w root of subtree
    w.right = v
    w.left = py

    return w

# Rrn where n is the number of red children of v's right child w
def Lr0(py):
    # LL rotation
    v = py.get_right()
    v.change_color()

    py.right = v.get_left()
    py.right.change_color()
    v.left = py

    py.left.deficient = False
    return v

# left node of w is red
def Lr1_case1(py):
    # LR rotation
    v = py.get_right()
    w = py.get_right().get_left()

    # reassign w's children
    v.left = w.get_right()
    py.right = w.get_left()

    # make w root of subtree
    w.right = v
    w.left = py

    py.left.deficient = False
    return w

# right node of w is red
def Lr1_case2(py):
    # rotation
    v = py.get_right()
    w = py.get_right().get_left()
    x = w.get_left() # the red node

    # reassign w's children
    w.left = x.get_right()
    py.right = x.get_left()

    # make w root of subtree
    x.right = v
    x.left = py

    py.left.deficient = False
    return w

def Lr2(py):
    # LR rotation
    v = py.get_right()
    w = py.get_right().get_left()
    x = w.get_left() # the red node

    # reassign w's children
    w.left = x.get_right()
    py.right = x.get_left()

    # make w root of subtree
    x.right = v
    x.left = py

    x.change_color() # now black and root of subtree
    py.left.deficient = False
    return w