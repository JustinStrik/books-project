# make a window that shows a smallish grey circle
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import os

# make a window that shows a smallish grey circle near the top middle. that's it.
#include the coordinates of the circle in the window title.
# make it display.


# canvas.create_oval(100, 100, 120, 10, fill="grey")
# canvas.create_oval(nodeX-10, nodeY-10, nodeX+10, nodeY+10, fill="grey")

def display_tree(root):

    this_level = []
    next_level = []
    level = 0

    tk = Tk()
    tk.title("Window Title")

    width = 400
    height = 400
    canvas = Canvas(tk, width=width, height=height)
    canvas.pack()

    # insert root into this_level
    # this_level.append(root)
    root.x = width/2
    root.y = 50
    if root.red:
        canvas.create_oval(root.x-10, root.y-10, root.x+10, root.y+10, fill="red")
    else:
        canvas.create_oval(root.x-10, root.y-10, root.x+10, root.y+10, fill="grey")
    canvas.create_text(root.x, root.y, text=root.book_id)

    if root.left.book_id != -1:
        this_level.append(root.left)
        root.left.update_coordinates(root.x - 40, root.y + 100)
        # draw a line from root to root.left, black if root.left is black, red if root.left is red
        if root.left.red:
            canvas.create_line(root.x, root.y, root.left.x, root.left.y, fill="red")
        else:
            canvas.create_line(root.x, root.y, root.left.x, root.left.y, fill="black")

    if root.right.book_id != -1:
        this_level.append(root.right)
        root.right.update_coordinates(root.x + 40, root.y + 100)
        # draw a line from root to root.right, black if root.right is black, red if root.right is red
        if root.right.red:
            canvas.create_line(root.x, root.y, root.right.x, root.right.y, fill="red")
        else:
            canvas.create_line(root.x, root.y, root.right.x, root.right.y, fill="black")
            
    level = 1

    while this_level:
        for node in this_level:
            if node.left.book_id != -1:
                next_level.append(node.left)
                # update coordinates
                node.left.update_coordinates(node.x - 40 * level / 3, node.y + 100)
                if node.left.red:
                    canvas.create_line(node.x, node.y, node.left.x, node.left.y, fill="red")
                else:
                    canvas.create_line(node.x, node.y, node.left.x, node.left.y, fill="black")

            if node.right.book_id != -1:
                next_level.append(node.right)
                node.right.update_coordinates(node.x + 40 * level / 3, node.y + 100)
                if node.right.red:
                    canvas.create_line(node.x, node.y, node.right.x, node.right.y, fill="red")
                else:
                    canvas.create_line(node.x, node.y, node.right.x, node.right.y, fill="black")

            if node.red:
                canvas.create_oval(node.x-10, node.y-10, node.x+10, node.y+10, fill="red")
            else:
                canvas.create_oval(node.x-10, node.y-10, node.x+10, node.y+10, fill="grey")
            # display node.book_id in the circle
            canvas.create_text(node.x, node.y, text=node.book_id)


        this_level = next_level
        next_level = []
        level += 1

    tk.mainloop()



