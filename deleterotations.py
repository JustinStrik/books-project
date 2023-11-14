# from bookdictionary import null_book

def delete_rotate(tree, node):
    left = node.left
    right = node.right
            
    if (right.deficient):
        # check to see if degree 1 ?
        if (left.red):
            # RRn
            w_red_children = 0
            w = left.right

            if (w.left.red):
                w_red_children += 1
            if (w.right.red):
                w_red_children += 1

            if (w_red_children == 0):
                node = Rr0(tree, node)
            elif (w_red_children == 1):
                if (w.left.red):
                    node = Rr1_case1(tree, node)
                else: # right is red
                    node = Rr1_case2(tree, node)
            else: # both children are red
                node = Rr2(tree, node)
        else: # left is black
            v = left
            v_red_children = 0

            if (v.left.red):
                v_red_children += 1
            if (v.right.red):
                v_red_children += 1

            if (v_red_children == 0):
                if (not node.red):
                    node = Rb0_case1(tree, node)
                    node.deficient = True
                else:
                    node = Rb0_case2(tree, node)
            elif (v_red_children == 1):
                if (v.left.red):
                    node = Rb1_case1(tree, node)
                else:
                    node = Rb1_case2(tree, node)
            elif (v_red_children == 2):
                node = Rb2(tree, node)
    else: # right subtree is not deficient, left must be (only reason this function is called)
        if (right.red):
            # RLn
            w_red_children = 0
            w = right.left

            if (w.left.red):
                w_red_children += 1
            if (w.right.red):
                w_red_children += 1

            if (w_red_children == 0):
                node = Lr0(tree, node)
            elif (w_red_children == 1):
                if (w.left.red):
                    node = Lr1_case1(tree, node)
                else:
                    node = Lr1_case2(tree, node)
            else: # both children are red
                node = Lr2(tree, node)
        else: # right is black
            v = right
            v_red_children = 0
        
            if (v.left.red):
                v_red_children += 1
            if (v.right.red):
                v_red_children += 1

            if (v_red_children == 0):
                if (not node.red):
                    node = Lb0_case1(tree, node)
                    node.deficient = True
                else:
                    node = Lb0_case2(tree, node)
            elif (v_red_children == 1):
                if (v.right.red):
                    node = Lb1_case1(tree, node)
                else:
                    node = Lb1_case2(tree, node)
            elif (v_red_children == 2):
                node = Lb2(tree, node)



    left.deficient = False
    right.deficient = False
    return node

# denoted by Xcn
# y is right child of py => X = R.
# Pointer to v is black => c = b.
# v has 1 red child => n = 1.

# py is black
def Rb0_case1(tree, py):
    py.left.change_color()
    py.right.deficient = False # right subtree isnt deficient
    py.deficient = True # now, py is deficient
    return py

# py is red
def Rb0_case2(tree, py):
    py.right.change_color()
    py.change_color()
    py.right.deficient = False # right subtree isnt deficient
    # no change to py deficiency
    return py

# left child of v is red
def Rb1_case1(tree, py):
    v = py.left

    py.left = v.right
    v.right = py

    v.left.change_color() # no longer red
    if py.red:
        py.right.change_color() # ? only change color if red?

    py.right.deficient = False # right subtree isnt deficient
    return v

# right child of v is red
def Rb1_case2(tree, py):
    # lr rotation
    v = py.left
    w = py.left.right
    w.change_color()

    # reassign w's children
    v.right = w.left
    py.left = w.right
    
    # make w root of subtree
    w.left = v
    w.right = py

    py.right.deficient = False 
    return w

def Rb2(tree, py):
    # lr rotation
    v = py.left
    w = py.left.right
    if (py.red != w.red): #?
        w.change_color() # now black

    # reassign w's children
    v.right = w.left
    py.left = w.right
    
    # make w root of subtree
    w.left = v
    w.right = py

    py.right.deficient = False 
    return w

# Rrn where n is the number of red children of v's right child w
def Rr0(tree, py):
    # LL rotation
    v = py.left
    v.change_color()

    py.left = v.right
    py.left.change_color()
    v.right = py

    py.right.deficient = False
    return v

# left node of w is red
def Rr1_case1(tree, py):
    # LR rotation
    v = py.left
    w = py.left.right

    # reassign w's children
    v.right = w.left
    py.left = w.right

    # make w root of subtree
    w.left = v
    w.right = py

    py.right.deficient = False
    return w

# right node of w is red
def Rr1_case2(tree, py):
    # rotation
    v = py.left
    w = py.left.right
    x = w.right # the red node

    # reassign w's children
    w.right = x.left
    py.left = x.right

    # make w root of subtree
    x.left = v
    x.right = py

    py.right.deficient = False
    return w

def Rr2(tree, py):
    # LR rotation
    v = py.left
    w = py.left.right
    x = w.right # the red node

    # reassign w's children
    w.right = x.left
    py.left = x.right

    # make w root of subtree
    x.left = v
    x.right = py

    x.change_color() # now black and root of subtree
    py.right.deficient = False
    return w

# py is black
def Lb0_case1(tree, py):
    py.right.change_color()
    py.left.deficient = False # left subtree isnt deficient
    py.deficient = True # now, py is deficient
    return py

# py is red
def Lb0_case2(tree, py):
    py.left.change_color()
    py.change_color()
    py.left.deficient = False # left subtree isnt deficient
    # no change to py deficiency
    return py

# right child of v is red
def Lb1_case1(tree, py):
    v = py.right

    py.right = v.left
    v.left = py

    v.right.change_color() # no longer red
    if py.red:
        py.left.change_color() # ? only change color if red?

    py.left.deficient = False # left subtree isnt deficient
    return v

# left child of v is red
def Lb1_case2(tree, py):
    # lr rotation
    v = py.right
    w = py.right.left
    w.change_color()

    # reassign w's children
    v.left = w.right
    py.right = w.left
    
    # make w root of subtree
    w.right = v
    w.left = py

    py.left.deficient = False 
    return w

def Lb2(tree, py):

    # lr rotation
    v = py.right
    w = py.right.left
    if (py.red != w.red): #?
        w.change_color() # now black

    # reassign w's children
    v.left = w.right
    py.right = w.left
    
    # make w root of subtree
    w.right = v
    w.left = py

    py.left.deficient = False 
    return w

# Rrn where n is the number of red children of v's right child w
def Lr0(tree, py):
    # LL rotation
    v = py.right
    v.change_color()

    py.right = v.left
    py.right.change_color()
    v.left = py

    py.left.deficient = False
    return v

# left node of w is red
def Lr1_case1(tree, py):
    # LR rotation
    v = py.right
    w = py.right.left

    # reassign w's children
    v.left = w.right
    py.right = w.left

    # make w root of subtree
    w.right = v
    w.left = py

    py.left.deficient = False
    return w

# right node of w is red
def Lr1_case2(tree, py):
    # rotation
    v = py.right
    w = py.right.left
    x = w.left # the red node

    # reassign w's children
    w.left = x.right
    py.right = x.left

    # make w root of subtree
    x.right = v
    x.left = py

    py.left.deficient = False
    return w

def Lr2(tree, py):
    # LR rotation
    v = py.right
    w = py.right.left
    x = w.left # the red node

    # reassign w's children
    w.left = x.right
    py.right = x.left

    # make w root of subtree
    x.right = v
    x.left = py

    x.change_color() # now black and root of subtree
    py.left.deficient = False
    return w