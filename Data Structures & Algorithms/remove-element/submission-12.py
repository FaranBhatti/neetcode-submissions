class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        given: integer arr called nums, and an integer value called val
        task: return all occurrences of val from nums in-place
        return: k where the first k elements of nums do not contain val
        """
        k = 0
        for index, num in enumerate(nums):
            if nums[index] != val:
                nums[k] = num
                k += 1
        
        return k