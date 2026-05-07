class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        given: a list of binaries called 'nums'
        return: maximum number of consecutive 1s in array
        """
        max_consecutive_ones = 0
        current_max_ones = 0
        for num in nums:
            
            if num:
                current_max_ones += 1

                if current_max_ones > max_consecutive_ones:
                    max_consecutive_ones = current_max_ones
            else:
                current_max_ones = 0
        
        return max_consecutive_ones