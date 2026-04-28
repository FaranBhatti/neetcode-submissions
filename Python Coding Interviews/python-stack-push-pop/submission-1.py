from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    # take a list of integers, return a new list of integers in the reverse order
    # pop() would take an element off of a stack and return that value
    reversed_list = []
    
    while len(arr) > 0:
        reversed_list.append(arr.pop())
    
    return reversed_list

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
