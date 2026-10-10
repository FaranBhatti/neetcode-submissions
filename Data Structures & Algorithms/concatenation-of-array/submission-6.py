class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Lets talk about whats happening under the hood.
        In ram there exists an array which is 'nums'.
        What we would like is a final array which is basically nums repeated twice.
        In python what would happen is we would make another array with double the size.
        Copy the elements of nums twice into it.
        this would be an O(n) operation as this is a copy into all the elements of this new array 'ans'
        the importance of knowing this is that this is bascically how dynamic arrays happen.
        under the hood arrays are dynamic because if the array size and the amount of elements is at its
        capacity a new one is created with double the size and the elements of the older one are copied
        over to this newer one. the older one is then deleted in python through a method called garbage
        collection automatically.
        """
        ans = nums + nums

        return ans