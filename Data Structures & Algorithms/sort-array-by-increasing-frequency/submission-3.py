class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # sort in increasing order based on FREQUENCY.
        # tie of frequency -> sort in DECREASING ORDER
        
        # count number of unique nums
        count = Counter(nums)

        nums.sort(key=lambda n:(count[n], -n))

        return nums