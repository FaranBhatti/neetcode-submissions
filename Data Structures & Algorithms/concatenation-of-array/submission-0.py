class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        given: integer array 'nums' of length 'n'.
        task: create an array 'ans' of length '2n' where ans is the concatenation of two nums arrays
        return: ans
        """
        ans = nums + nums

        return ans
