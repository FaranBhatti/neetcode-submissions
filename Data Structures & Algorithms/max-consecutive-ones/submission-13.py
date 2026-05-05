class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num_count, current_max_num_count = 0, 0
        
        for num in nums:
            if num:
                current_max_num_count += 1

                if current_max_num_count > max_num_count:
                    max_num_count = current_max_num_count
            else:
                current_max_num_count = 0

        return max_num_count