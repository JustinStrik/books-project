from time import *

class ReservationNode:
    def __init__(self, book, patron_id, patron_priority):
        self.book = book
        self.patron_id = patron_id
        self.patron_priority = patron_priority
        self.time = time()

    def add_child(self, node):
        self.children.append(node)

def move_left(pos):
    if (pos == 0):
        return 1
    return pos * 2

def move_right(pos):
    if (pos == 0):
        return 2
    return pos * 2 + 1
    
class ReservationHeap:
    heap = []
    def __init__(self):
        self.heap = []
        self.root = None

    # takes in position in heap array
    def get_parent(self, pos):
        if (pos == 0):
            return None
        elif (pos == 2):
            return self.heap[0]
        
        return self.heap[pos // 2] # double slash is integer division, so floor
    
    def get_left(self, pos):
        if (pos * 2 >= len(self.heap)):
            return None
        
        elif (pos == 0):
            if (len(self.heap) == 1):
                return None
            return self.heap[1]
        
        return self.heap[pos * 2]
    
    def get_right(self, pos):
        if (pos * 2 + 1 >= len(self.heap)):
            return None
        
        elif (pos == 0):
            if (len(self.heap) < 3):
                return None
            return self.heap[2]
        
        return self.heap[pos * 2 + 1]
    
    def swap(self, pos1, pos2):
        # if 0,0, swap 0 and 1
        # if 0,1, swap 0 and 2 since 0 multiplied by 2 is 0
        if (pos1 == 0):
            if (pos2 == 1):
                pos2 = 2
            else:
                pos2 = 1

        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def insert(self, reservation_node):
        self.heap.append(reservation_node)

        pos = len(self.heap) - 1
        # time shouldnt matter on an insert since it will always be the most recent
        while (pos > 0 and reservation_node.patron_priority <= self.get_parent(pos).patron_priority):
            # if equal, check to see if the time is less
            if (reservation_node.patron_priority == self.get_parent(pos).patron_priority):
                if (reservation_node.time < self.get_parent(pos).time):
                    self.swap(pos, pos // 2)
                    pos = pos // 2
                    continue
                else:
                    break
            # not equal, just less: swap
            self.swap(pos, pos // 2)
            pos = pos // 2

    def remove(self):
        if (len(self.heap) == 0):
            return None

        removed = self.heap[0]
        if (len(self.heap) > 1):
            self.heap[0] = self.heap.pop() # remove last element and put it at the beginning
            pos = 0

            done_heapifying = False
            while (pos < len(self.heap) or not done_heapifying):
                # if the left child is less than the right child, swap with the left child
                # if the right child is less than the left child, swap with the right child
                # check for nulls

                if (self.get_left(pos) != None and self.get_right(pos) != None):
                    if (self.get_left(pos).patron_priority < self.get_right(pos).patron_priority):
                        if (self.heap[pos].patron_priority > self.get_left(pos).patron_priority):
                            self.swap(pos, pos * 2)
                            pos = move_left(pos)
                            continue
                        elif (self.heap[pos].patron_priority == self.get_left(pos).patron_priority):
                            if (self.heap[pos].time > self.get_left(pos).time):
                                self.swap(pos, pos * 2)
                                pos = move_left(pos)
                                continue
                        else:
                            done_heapifying = True
                            break
                    else:
                        if (self.heap[pos].patron_priority > self.get_right(pos).patron_priority):
                            self.swap(pos, pos * 2 + 1)
                            pos = move_right(pos)
                            continue
                        elif (self.heap[pos].patron_priority == self.get_right(pos).patron_priority):
                            if (self.heap[pos].time > self.get_right(pos).time):
                                self.swap(pos, pos * 2 + 1)
                                pos = move_right(pos)
                                continue
                        else:
                            done_heapifying = True
                            break
                # its possible for left to not be null, but its not possible for right and NOT left to be null
                elif (self.get_left(pos) != None): 
                    if (self.heap[pos].patron_priority > self.get_left(pos).patron_priority):
                        self.swap(pos, pos * 2)
                        pos = move_left(pos)
                        continue
                    elif (self.heap[pos].patron_priority == self.get_left(pos).patron_priority):
                        if (self.heap[pos].time > self.get_left(pos).time):
                            self.swap(pos, pos * 2)
                            pos = move_left(pos) # should always be the end, since if right is null, then this left was last
                            continue
                    else:
                        done_heapifying = True
                        break

                # if (self.get_left(pos) != None):
                #     if (self.heap[pos].patron_priority > self.get_left(pos).patron_priority):
                #         self.swap(pos, pos * 2)
                #         pos = move_left(pos)
                #         continue
                #     # if they're equal, break the tie with their time
                #     elif (self.heap[pos].patron_priority == self.get_left(pos).patron_priority):
                #         # frst come first serve priority for time
                #         # so if the current node's time is greater than the left node's time, swap
                #         if (self.heap[pos].time > self.get_left(pos).time):
                #             self.swap(pos, pos * 2)
                #             pos = move_left(pos)
                #             continue

                # elif (self.get_right(pos) != None):
                #     if (self.heap[pos].patron_priority > self.get_right(pos).patron_priority):
                #         self.swap(pos, pos * 2 + 1)
                #         pos = move_right(pos)
                #         continue
                #     # if they're equal, break the tie with their time
                #     elif (self.heap[pos].patron_priority == self.get_right(pos).patron_priority):
                #         if (self.heap[pos].time > self.get_right(pos).time):
                #             self.swap(pos, pos * 2 + 1)
                #             pos = move_right(pos)
                #             continue
                #     else:
                #         done_heapifying = True
                #         break
                # else:
                #     done_heapifying = True
                #     break
                

                if (pos == 0):
                    pos += 1
                else:
                    pos = pos * 2

        return removed

    # def print_reservations(self):
    #     for reservation in self.heap:
    #         print(reservation.patron_id, reservation.patron_priority)

            

