class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # given an array which is a list of integers
        # say youre on the first element, whats the greatest value in the rest of the list? replace that element youre on with it

        # have      arr=[2,4,5,3,1,2]
        # return    [3, -1]
        current_max_val = -1
        for index in range(len(arr) - 1, -1, -1):
            # check the value at that location and replace it with the stored max
            # update the maximum if the element im replacing is even larger
            replaced_val = arr[index]
            arr[index] = current_max_val

            if replaced_val > current_max_val:
                current_max_val = replaced_val
        
        return arr