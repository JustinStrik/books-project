from time import *

class ReservationNode:
    def __init__(self, book, patron_id, patron_priority):
        self.book = book
        self.patron_id = patron_id
        self.patron_priority = patron_priority
        self.time = time()

    def add_child(self, node):
        self.children.append(node)

# starts at 0, so left child is 1, right child is 2, etc
def move_left(pos):
    return pos * 2 + 1

def move_right(pos):
    return pos * 2 + 2
    
class ReservationHeap:
    heap = []
    def __init__(self):
        self.heap = []
        self.root = None

    # takes in position in heap array
    def get_parent(self, pos):
        return self.heap[(pos - 1) // 2] # double slash is integer division, so floor
    
    def get_left(self, pos):
        if (pos * 2 + 1 >= len(self.heap)):
            return None
        
        return self.heap[pos * 2 + 1]
    
    def get_right(self, pos):
        if (pos * 2 + 2 >= len(self.heap)):
            return None
        
        return self.heap[pos * 2 + 2]
    
    # swaps two nodes in the heap for heapify
    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def insert(self, reservation_node):
        self.heap.append(reservation_node)

        pos = len(self.heap) - 1
        # time shouldnt matter on an insert since it will always be the most recent
        while (pos > 0 and reservation_node.patron_priority <= self.get_parent(pos).patron_priority):
            # if equal, check to see if the time is less
            if (reservation_node.patron_priority == self.get_parent(pos).patron_priority):
                if (reservation_node.time < self.get_parent(pos).time):
                    self.swap(pos, (pos - 1) // 2)
                    pos = (pos - 1) // 2
                    continue
                else:
                    break
            # not equal, just less: swap
            self.swap(pos, (pos - 1) // 2)
            pos = (pos - 1) // 2

    def remove(self):
        if (len(self.heap) == 0):
            return None

        removed = self.heap[0]
        if (len(self.heap) > 1):
            self.heap[0] = self.heap.pop() # remove last element and put it at the beginning
            pos = 0

            done_heapifying = False
            while (pos < len(self.heap) and not done_heapifying):
                # if the left child priority is less than the right child, swap with the left child when less than the parent
                # if the right child is less than the left child, swap with the right child
                # check for nulls
                if (self.get_left(pos) != None and self.get_right(pos) != None):
                    if (self.get_left(pos).patron_priority < self.get_right(pos).patron_priority):
                        # if parent is greater than left child, swap
                        if (self.heap[pos].patron_priority > self.get_left(pos).patron_priority):
                            self.swap(pos, pos * 2 + 1)
                            pos = move_left(pos)
                            continue
                        # if equal, break the tie with their time
                        elif (self.heap[pos].patron_priority == self.get_left(pos).patron_priority):
                            if (self.heap[pos].time > self.get_left(pos).time):
                                self.swap(pos, pos * 2 + 1)
                                pos = move_left(pos)
                                continue
                        # if the lesser (left, in this case) child is greater than the parent, then stop heapifying
                        else:
                            done_heapifying = True
                            break
                    # if the right child is less than the left child, try and swap with the right child
                    elif (self.get_left(pos).patron_priority > self.get_right(pos).patron_priority):
                        if (self.heap[pos].patron_priority > self.get_right(pos).patron_priority):
                            self.swap(pos, pos * 2 + 2)
                            pos = move_right(pos)
                            continue
                        elif (self.heap[pos].patron_priority == self.get_right(pos).patron_priority):
                            # if was inserted after child, then swap with the right child
                            if (self.heap[pos].time > self.get_right(pos).time):
                                self.swap(pos, pos * 2 + 2)
                                pos = move_right(pos)
                                continue
                        else:
                            # if the lesser (right, in this case) child is greater than the parent, then stop heapifying pls
                            done_heapifying = True
                            break
                    else: # if they're equal
                        if (self.get_left(pos).time < self.get_right(pos).time):
                            if (self.heap[pos].patron_priority > self.get_left(pos).patron_priority):
                                self.swap(pos, pos * 2 + 1)
                                pos = move_left(pos)
                                continue
                            elif (self.heap[pos].patron_priority == self.get_left(pos).patron_priority):
                                if (self.heap[pos].time > self.get_left(pos).time):
                                    self.swap(pos, pos * 2 + 1)
                                    pos = move_left(pos)
                                    continue
                            else:
                                done_heapifying = True
                                break
                        else:
                            if (self.heap[pos].patron_priority > self.get_right(pos).patron_priority):
                                self.swap(pos, pos * 2 + 2)
                                pos = move_right(pos)
                                continue
                            elif (self.heap[pos].patron_priority == self.get_right(pos).patron_priority):
                                if (self.heap[pos].time > self.get_right(pos).time):
                                    self.swap(pos, pos * 2 + 2)
                                    pos = move_right(pos)
                                    continue
                            else:
                                done_heapifying = True
                                break
                            
                # the first if checks if they're both null.    
                # its possible for left to not be null, but its not possible for right and NOT left to be null
                elif (self.get_left(pos) != None): 
                    if (self.heap[pos].patron_priority > self.get_left(pos).patron_priority):
                        self.swap(pos, pos * 2 + 1)
                        pos = move_left(pos)
                        continue
                    elif (self.heap[pos].patron_priority == self.get_left(pos).patron_priority):
                        if (self.heap[pos].time > self.get_left(pos).time):
                            self.swap(pos, pos * 2 + 1)
                            pos = move_left(pos) # should always be the end, since if right is null, then this left was last
                            continue
                    else:
                        done_heapifying = True
                        break
                

                done_heapifying = True # if here, then did not break and is done heapifying

        return removed

    # def print_reservations(self):
    #     for reservation in self.heap:
    #         print(reservation.patron_id, reservation.patron_priority)

            

