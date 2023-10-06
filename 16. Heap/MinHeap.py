import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def size(self):
        return len(self.heap)

# Example Usage:
min_heap = MinHeap()
min_heap.push(3)
min_heap.push(1)
min_heap.push(4)
min_heap.push(2)

print("Min Heap:", min_heap.heap)

while min_heap.size() > 0:
    print("Pop:", min_heap.pop())

