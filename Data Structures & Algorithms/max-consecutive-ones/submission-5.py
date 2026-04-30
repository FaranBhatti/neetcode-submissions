class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_nums = 0
        current_max_nums = 0
        for num in nums:
            if num:
                current_max_nums += 1
                if current_max_nums > max_consecutive_nums:
                    max_consecutive_nums = current_max_nums
            else:
                current_max_nums = 0
        
        return max_consecutive_nums