import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    """
    given: list of numbers called nums
    task: take list of integers and return integers in reverse sorted order. use tuples
    return: list of integers that are sorted
    """
    reverse_sorted_heap = []
    for num in nums:
        heapq.heappush(reverse_sorted_heap, (-num, num))
    
    return [heapq.heappop(reverse_sorted_heap)[1] for _ in range(len(reverse_sorted_heap))]



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
