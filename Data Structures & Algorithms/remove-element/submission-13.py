class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        given: array of integers 'nums, and integer to remove 'val'
        task: remove in-place = modify original list.
        return: k such that the first k elements of nums do not contain val
        """
        k = 0

        for index, num in enumerate(nums):
            if num != val:
                nums[k] = num
                k += 1
        
        return k