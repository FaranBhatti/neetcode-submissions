class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Efficient solution:
        Since we're trying to start from the right side we just need to compare the value next to it
        - start condition for currentMax = -1
        1. loop over array from the right side.
        2. check newMax and compare it to the currentMax. if its greater assign it to the currentMax
        3. assign currentMax to that location
        """
        currentMax = -1
        newMax = 0

        for i in reversed(range(len(arr))):
            if arr[i] > currentMax:
                newMax = arr[i]
            
            arr[i] = currentMax
            currentMax = newMax
        
        return arr



