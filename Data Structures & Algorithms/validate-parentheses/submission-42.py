class Solution:
    def isValid(self, s: str) -> bool:
        """
        Efficient solution:
        - every open bracket closed by same type of closed bracket
        - order matters (order in which they're closed)
        - every close has a corresponding open of the same type

        1. iterate through string
        2. add each open bracket to stack
        3. remove open bracket whenever bracket corresponding to same closing type appears

        if stack empty -> valid string
        if stack not empty -> invalid string 
        """
        openToClosed = {"(": ")", "{": "}", "[": "]"}
        
        stack = []

        # iterate over each bracket that comes in string
        for bracket in s:
            # check if bracket is an opening bracket
            if bracket in openToClosed:
                # add into stack if opening bracket
                stack.append(bracket)
            # bracket is a closing bracket
            else:
                # check if closing bracket is the correct bracket for corresponding opening bracket
                if not stack or openToClosed[stack[-1]] != bracket:
                    return False
                else:
                    stack.pop()
        
        return not stack

