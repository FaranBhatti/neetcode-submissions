class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, max_count_ones = 0, 0

        for num in nums:
            if num:
                count += 1
            else:
                if count > max_count_ones:
                    max_count_ones = count
                count = 0
        
        if count > max_count_ones:
            max_count_ones = count

        return max_count_ones