class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max_val = -1
        for index in range(len(arr) - 1, -1, -1):

            replaced_val = arr[index]
            arr[index] = current_max_val

            if replaced_val > current_max_val:
                current_max_val = replaced_val
        
        return arr