from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    # you have: 2D list of integers return list which contains the maximum element from each sublist in order they appear in the input list
    max_in_each_list = []
    for integers_list in nested_arr:
        max_value = 0
        for integer in integers_list:
            if integer > max_value:
                max_value = integer
        
        max_in_each_list.append(max_value)
    
    return max_in_each_list


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
