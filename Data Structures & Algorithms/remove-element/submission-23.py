class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # supposed we have [0, 1, 3, 3] and val = 3 return k = 2 and nums = [0, 1, 0, 0]
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k