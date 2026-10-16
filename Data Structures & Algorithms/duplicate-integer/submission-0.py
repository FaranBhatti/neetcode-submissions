class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = {}

        for num in nums:
            if num in uniqueNums:
                return True
            else:
                uniqueNums[num] = 1
        return False