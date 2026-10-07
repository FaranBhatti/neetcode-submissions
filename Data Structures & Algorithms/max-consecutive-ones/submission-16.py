class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, max_count_ones = 0, 0

        for num in nums:
            if num:
                count += 1
                if count > max_count_ones:
                    max_count_ones = count
            else:
                count = 0


        return max_count_ones