import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    """
    pop all elements from the heap and return them in a list in the order that they were popped
    """
    return [heapq.heappop(heap) for index in range(len(heap))]


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
