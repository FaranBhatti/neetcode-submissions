class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two things: return k where k are non-val elements, shift array so the first k elements are non-val elements

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k