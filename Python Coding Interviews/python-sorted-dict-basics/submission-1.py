from typing import List
from sortedcontainers import SortedDict


def remove_keys(sorted_dict: SortedDict[str, int], keys: List[str]) -> SortedDict[str, int]:
    """
    have: a sorted dictionary called 'sorted_dict', a list of strings which are keys called 'keys'
    task: remove key-value pairs associated with thsoe keys from the dict
    return: return modified sorted dictionary 'sorted_dict'
    """
    for key in keys:
        if key in sorted_dict:
            sorted_dict.pop(key)
    
    return sorted_dict


def get_values_before_target(sorted_dict: SortedDict[str, int], target: str) -> List[int]:
    """
    have: sorted dictionary called 'sorted_dict', target key called 'target'
    task: obtain list of values with keys that come before the 'target' key in 'sorted_dict'
    return: list of values
    """
    idx = sorted_dict.index(target)

    return list(sorted_dict.values()[:idx])

# do not modify below this line
print(remove_keys(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35}), ['Bob']))
print(remove_keys(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), ['Bob', 'David']))
print(remove_keys(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40, 'Eve': 45}), ['Alice', 'Eve']))

print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35}), 'Bob'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'David'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'Charlie'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'Bob'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'Alice'))
