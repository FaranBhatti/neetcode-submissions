class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num_count = 0
        num_count = 0
        
        for num in nums:
            if num:
                num_count += 1
            else:
                num_count = 0

            if num_count > max_num_count:
                max_num_count = num_count

        return max_num_count