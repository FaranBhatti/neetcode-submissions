from typing import List
from sortedcontainers import SortedSet


def get_first_three(sorted_set: SortedSet[int], nums1: List[int], nums2: List[int]) -> List[int]:
    """
    given: 'sorted_set', two lists of integers 'nums1' and 'nums2'
    task: add 'nums1' to 'sorted_set', then remove elements in 'nums2' that exists in 'sorted_set'
    return: the first three elements of the sorted set as a list of int
    """
    sorted_set.update(nums1)
    
    sorted_set.difference_update(nums2)
    
    return list(sorted_set[:3])


# do not modify below this line
print(get_first_three(SortedSet(), [1, 2, 3], [4]))
print(get_first_three(SortedSet([1, 4, 7, 2, 8, 9]), [10], [1, 7, 2]))
print(get_first_three(SortedSet([1, 2, 3, 7]), [], [4, 5, 6]))
print(get_first_three(SortedSet([1, 2, 3, 4, 5, 6, 7, 8, 9]), [10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
