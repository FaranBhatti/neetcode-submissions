class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        given: integer array nums, and integer val
        return: the count k while removing all occurrences of val from nums in-place
        """
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k