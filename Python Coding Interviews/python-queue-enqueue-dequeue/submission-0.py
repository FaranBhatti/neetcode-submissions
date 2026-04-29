from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    # take a list of ints and an integer k
    # convert the list into a deque, then rotate the values in the list to the left by k steps and return resulting queue
    queue = deque(arr)
    while k > 0:
        element = queue.popleft()
        queue.append(element)
        k -= 1
    
    return queue



# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
