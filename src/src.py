class MinHeap:
    def __init__(self):
        self.heap = []

    def get_parent(self, i):
        return (i - 1) // 2

    def get_left_child(self, i):
        return 2 * i + 1

    def get_right_child(self, i):
        return 2 * i + 2

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
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while self.has_parent(i) and self.heap[i] < self.heap[self.get_parent(i)]:
            self.swap(i, self.get_parent(i))
            i = self.get_parent(i)

    def delete_root(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.swap(0, len(self.heap) - 1)
        self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self, i):
        while self.has_left_child(i):
            min_child_ind = self.get_min_child_index(i)
            if min_child_ind == -1:
                break
            if self.heap[i] > self.heap[min_child_ind]:
                self.swap(i, min_child_ind)
                i = min_child_ind
            else:
                break

    def get_min_child_index(self, i):
        left_child = self.get_left_child(i)
        right_child = self.get_right_child(i)

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[left_child]:
            return right_child
        return left_child if left_child < len(self.heap) else -1

    def print_heap(self):
        if not self.heap:
            print("Empty heap")
            return

        height = (len(self.heap) - 1).bit_length()  
        level = 0
        max_width = 2 ** height - 1  

        nodes_in_level = 1  
        for i in range(len(self.heap)):
            if i == 2 ** level - 1:
                print()  
                nodes_in_level *= 2
                level += 1
            print(f"{self.heap[i]:^3}", end=" " * (max_width // nodes_in_level))

        print()  


        ### TEST
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(10)
    heap.insert(7)
    heap.insert(9)
    heap.insert(6)
    heap.insert(3)
    heap.insert(5)
    heap.insert(8)
    heap.print_heap()

    print("Deleting root:", heap.delete_root())
    heap.print_heap()