# LLr, RRr, LLb, RRb, LRb, RLb
def insert_rotate(tree, node):
    left = node.left
    right = node.right
    if (left.invalid):
        if (left.left.red):
            if (right.red):
                node = LLr(tree, node)
            else:
                node = LLb(tree, node)
        elif not right.red:
            node = LRb(tree, node)
        else:
            node = LRr(tree, node)
            
    if (right.invalid):
        if (right.right.red):
            if (left.red):
                node = RRr(tree, node)
            else:
                node = RRb(tree, node)
        # right is invalid, left is red
        elif not left.red:
            node = RLb(tree, node)
        else:
            node = RLr(tree, node)

    left.invalid = False
    right.invalid = False
    return node
    

# declare functions for all rotations
def LLr(tree, gp):
    if not gp.is_root:
        gp.change_color() 
    gp.left.change_color()
    gp.right.change_color()
    
        # requires continue rebalancing
        # will happen automatically because its recursive
    return gp

def RRr(tree, gp):
    if not gp.is_root:
        gp.change_color()
    gp.right.change_color()
    gp.left.change_color()
    
    return gp

def LLb(tree, gp):
    if (gp.is_root):
        # change root
        tree.root = gp.left
        gp.is_root = False
        tree.root.is_root = True

    y = gp.left
    gp.left = y.right
    y.right = gp
    y.change_color()
    y.right.change_color() # gp
    return y

def RRb(tree, gp):
    if (gp.is_root):
        # change root
        tree.root = gp.right
        gp.is_root = False
        tree.root.is_root = True

    y = gp.right
    gp.right = y.left
    y.left = gp
    # y.change_color()
    y.change_color()
    y.left.change_color()
    return y

def LRb(tree, gp):
    if (gp.is_root):
        # change root
        root = gp.left.right
        gp.is_root = False
        root.is_root = True

    # test to see whats variables
    # gp is z
    # reassign y's children before it gets moved up
    x = gp.left
    y = gp.left.right

    x.right = y.left
    gp.left = y.right
    y.left = x
    y.right = gp
    gp.change_color()
    y.change_color()
    return y
    



def RLb(tree, gp):
    if (gp.is_root):
        # change root
        root = gp.right.left
        gp.is_root = False
        root.is_root = True
    
    x = gp.right
    y = gp.right.left

    x.left = y.right
    gp.right = y.left
    y.right = x
    y.left = gp
    gp.change_color()
    y.change_color()

    return y

def RLr(tree, gp):
    # no movements, change all colors
    if (not gp.is_root):
        gp.change_color()
    gp.right.change_color()
    gp.left.change_color()
    # gp.right.left.change_color() # remains red
    return gp

def LRr(tree, gp):
    # no movements, change all colors
    if (not gp.is_root):
        gp.change_color()
    gp.left.change_color()
    gp.right.change_color()
    # gp.left.right.change_color() # remains red
    return gp
    