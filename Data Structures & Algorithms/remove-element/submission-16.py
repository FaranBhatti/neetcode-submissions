class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        in-place = modify original array 'nums' return k such that k elements of nums do not contain val
        """
        k = 0

        for index, num in enumerate(nums):
            if nums[index] != val:
                nums[k] = num
                k += 1
        
        return k