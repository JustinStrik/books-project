from time import *

class ReservationNode:
    def __init__(self, book, patron_id, patron_priority):
        self.book = book
        self.patron_id = patron_id
        self.patron_priority = patron_priority
        self.time = time()

    def add_child(self, node):
        self.children.append(node)

class ReservationHeap:
    heap = []
    def __init__(self):
        self.heap = []
        self.root = None

    # takes in position in heap array
    def get_parent(self, pos):
        return self.heap[pos // 2] # double slash is integer division, so floor
    
    def get_left(self, pos):
        if (pos * 2 >= len(self.heap)):
            return None
        return self.heap[pos * 2]
    
    def get_right(self, pos):
        if (pos * 2 + 1 >= len(self.heap)):
            return None
        return self.heap[pos * 2 + 1]
    
    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def insert(self, reservation_node):
        self.heap.append(reservation_node)

        pos = len(self.heap) - 1
        while (pos > 0 and reservation_node.patron_priority < self.get_parent(pos).patron_priority):
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

                if (self.get_left(pos) != None):
                    if (self.heap[pos].patron_priority > self.get_left(pos).patron_priority):
                        self.swap(pos, pos * 2)
                        pos *= 2
                        continue
                    # if they're equal, break the tie with their time
                    elif (self.heap[pos].patron_priority == self.get_left(pos).patron_priority):
                        # frst come first serve priority for time
                        # so if the current node's time is greater than the left node's time, swap
                        if (self.heap[pos].time > self.get_left(pos).time):
                            self.swap(pos, pos * 2)
                            pos *= 2
                            continue

                if (self.get_right(pos) != None):
                    if (self.heap[pos].patron_priority > self.get_right(pos).patron_priority):
                        self.swap(pos, pos * 2 + 1)
                        pos = pos * 2 + 1
                        continue
                    # if they're equal, break the tie with their time
                    elif (self.heap[pos].patron_priority == self.get_right(pos).patron_priority):
                        if (self.heap[pos].time > self.get_right(pos).time):
                            self.swap(pos, pos * 2 + 1)
                            pos = pos * 2 + 1
                            continue
                    else:
                        done_heapifying = True
                        break
                

                if (pos == 0):
                    pos += 1
                else:
                    pos = pos * 2

        return removed

    # def print_reservations(self):
    #     for reservation in self.heap:
    #         print(reservation.patron_id, reservation.patron_priority)

            

