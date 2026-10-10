class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        currentMax = 0

        for num in nums:
            if num:
                count += 1
                if count > currentMax:
                    currentMax = count
            else:
                count = 0
        
        return currentMax