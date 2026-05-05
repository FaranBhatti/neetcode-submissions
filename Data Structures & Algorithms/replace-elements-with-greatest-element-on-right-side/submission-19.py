class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max_value = -1
        for index in range(len(arr) - 1, -1, -1):
            replaced_val = arr[index]
            arr[index] = current_max_value

            if replaced_val > current_max_value:
                current_max_value = replaced_val
        return arr