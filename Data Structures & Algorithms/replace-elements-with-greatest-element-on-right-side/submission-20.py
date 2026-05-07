class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        given: given an array 'arr' integers
        task: replace last element with -1, replace every element in arr with greatest element among the elements to its right
        return: modified 'arr'
        """
        current_max_num = -1
    
        for index in range(len(arr) - 1, -1, -1):
            replaced_val = arr[index]
            arr[index] = current_max_num
            
            if replaced_val > current_max_num:
                current_max_num = replaced_val
        
        return arr