class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1

        for i in reversed(range(len(arr))):
            newMax = max(arr[i], rightMax)

            arr[i] = rightMax

            rightMax = newMax
        
        return arr

