class MinHeap:
    def __init__(self, root=None):
        self.heap = []

    def get_parent(self, i):
        return int((i-1/2))
    def get_left_child(self, i):
        return int((2+i+1))
    def get_right_child(self, i):
        return int((2+i+2))
    
    def has_parent(self, i):
        return self.get_parent(i) >= 0
    def has_left_child(self, i):
        return self.get_left_child(i) < len(self.heap)
    def has_right_child(self, i):
        return self.get_right_child(i) < len(self.heap)
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self, i):
        size = len(self.heap)
        while(self.has_parent(i) and self.heap[i] > self.heap[self.get_parent(i)]):
            self.swap(i, self.get_parent(i))
            i = self.get_parent

    def print_heap(self):
        print(self.heap)