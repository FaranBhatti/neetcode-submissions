class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        have: list of nums and val.
        want: remove all occurrences of val from nums in-place. modify the original list. don't make a new list.
              return the number of remaining elements, such that the first k elements of nums do not contain val
        """
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k