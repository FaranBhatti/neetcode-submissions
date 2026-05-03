class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        given: binary array nums
        return: max number of consecutive 1s in array
        """
        max_num_count = 0
        num_count = 0
        
        for num in nums:
            if num == 1:
                num_count += 1
            else:
                num_count = 0

            if num_count > max_num_count:
                max_num_count = num_count

        return max_num_count