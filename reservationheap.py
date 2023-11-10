class ReservationNode:
    def __init__(self, book, patron_id, patron_priority):
        self.book = book
        self.patron_id = patron_id
        self.patron_priority = patron_priority

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
        return self.heap[pos * 2]
    
    def get_right(self, pos):
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
        self.heap[0] = self.heap.pop() # remove last element and put it at the beginning
        pos = 0

        while (pos < self.heap.__len__):
            if (self.heap[pos] > self.get_right(pos)):
                self.swap(pos, pos * 2)
                break
            elif (self.heap[pos] > self.get_right(pos + 1)):
                self.swap(pos, pos * 2)
                break

            if (pos == 0):
                pos += 1
            else:
                pos = pos * 2

            

