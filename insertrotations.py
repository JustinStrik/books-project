# LLr, RRr, LLb, RRb, LRb, RLb
def insert_rotate(node):
    left = node.left
    right = node.right
    if (left.invalid):
        if (left.left.red):
            if (right.red):
                node = LLr(node)
            else:
                node = LLb(node)
        elif not right.red:
            node = LRb(node)
        else:
            node = LRr(node)
            
    if (right.invalid):
        if (right.right.red):
            if (left.red):
                node = RRr(node)
            else:
                node = RRb(node)
        # right is invalid, left is red
        elif not left.red:
            node = RLb(node)
        else:
            node = RLr(node)

    left.invalid = False
    right.invalid = False
    return node
    

# declare functions for all rotations
def LLr(gp):
    if not gp.is_root:
        gp.change_color() 
    gp.left.change_color()
    gp.right.change_color()
    
        # requires continue rebalancing
        # will happen automatically because its recursive
    return gp

def RRr(gp):
    if not gp.is_root:
        gp.change_color()
    gp.right.change_color()
    gp.left.change_color()
    
    return gp

def LLb(gp):
    if (gp.is_root):
        # change root
        gp.left.is_root = True
        gp.is_root = False

    y = gp.left # will be new root
    gp.left = y.right
    y.right = gp
    y.change_color()
    y.right.change_color() # gp
    return y

def RRb(gp):
    if (gp.is_root):
        # change root
        gp.is_root = False
        gp.right.is_root = True

    y = gp.right
    gp.right = y.left
    y.left = gp
    # y.change_color()
    y.change_color()
    y.left.change_color()
    return y

def LRb(gp):
    if (gp.is_root):
        # change root
        gp.left.right.is_root = True
        gp.is_root = False

    # test to see whats variables
    # gp is z
    # reassign y's children before it gets moved up
    x = gp.left
    y = gp.left.right # will be new root

    x.right = y.left
    gp.left = y.right
    y.left = x
    y.right = gp
    gp.change_color()
    y.change_color()
    return y
    



def RLb(gp):
    if (gp.is_root):
        # change root
        gp.right.left.is_root = True
        gp.is_root = False
    
    x = gp.right
    y = gp.right.left # will be new root

    x.left = y.right
    gp.right = y.left
    y.right = x
    y.left = gp
    gp.change_color()
    y.change_color()

    return y

def RLr(gp):
    # no movements, change all colors
    if (not gp.is_root):
        gp.change_color()
    gp.right.change_color()
    gp.left.change_color()
    # gp.right.left.change_color() # remains red
    return gp

def LRr(gp):
    # no movements, change all colors
    if (not gp.is_root):
        gp.change_color()
    gp.left.change_color()
    gp.right.change_color()
    # gp.left.right.change_color() # remains red
    return gp
    