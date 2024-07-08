
class CustomMinHeap:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None]*capacity

        # Current number of elements in the Heap.
        self.size = 0

    def _get_parent_index(self, currentIndex):
        """Getting parent index of current node."""
        return (currentIndex - 1) // 2

    def _get_left_child_index(self, currentIndex):
        """Getting the left child index of a current node."""
        return 2 * currentIndex + 1

    def _get_right_child_index(self, currentIndex):
        """Getting the right child index of a current node."""
        return 2 * currentIndex + 2

    def _has_parent(self, currentIndex):
        """Returns bool type depending on whether there is a parent or not."""
        return self._get_parent_index(currentIndex) >= 0

    def _has_left_child(self, currentIndex):
        """Returns bool type depending on whether there is a left child or not."""
        return self._get_left_child_index(currentIndex) < self.size

    def _has_right_child(self, currentIndex):
        """Returns bool type depending on whether there is a right child or not."""
        return self._get_right_child_index(currentIndex) < self.size

    def _get_parent_value(self, currentIndex):
        return self.storage[self._get_parent_index(currentIndex)]

    def _get_left_child_value(self, currentIndex):
        return self.storage[self._get_left_child_index(currentIndex)]

    def _get_right_child_value(self, currentIndex):
        return self.storage[self._get_right_child_index(currentIndex)]

    def _is_heap_full(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        tmp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = tmp

    def _heapify_up(self):
        currentIndex = self.size - 1
        currentValue = self.storage[currentIndex]

        # Loop until there is a parent and the parent value is greater than current node value.
        while self._has_parent(currentIndex) and (self._get_parent_value(currentIndex) > currentValue):

            parentIndex = self._get_parent_index(currentIndex)

            # Swap.
            self.swap(index1=parentIndex, index2=currentIndex)

            # Update vars.
            currentIndex = self._get_parent_index(currentIndex)
            currentValue = self.storage[currentIndex]

    def insert(self, data):

        if self._is_heap_full():
            raise Exception("Heap if Full")

        self.storage[self.size] = data
        self.size += 1

        self._heapify_up()

    def print_heap(self):
        print(self.storage)


heap_obj = CustomMinHeap(10)
heap_obj.print_heap()

heap_obj.insert(10)
heap_obj.print_heap()

heap_obj.insert(5)
heap_obj.print_heap()

heap_obj.insert(15)
heap_obj.print_heap()

heap_obj.insert(2)
heap_obj.print_heap()
