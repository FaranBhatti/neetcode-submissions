from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    # given a list of integers in arr and an integer k
    # convert list into deque
    # rotate values in the list to the right by k steps
    # return resulting deque
    queue = deque(arr)

    # find out how many rotations to do if arr is 5 and we do 6 rotatiosn thats the same as 1 rotation
    rotations = k % len(arr)

    for _ in range(rotations):
        element = queue.pop()
        queue.appendleft(element)
        
    return queue


# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
