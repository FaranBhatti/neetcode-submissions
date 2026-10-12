class Solution:
    def isValid(self, s: str) -> bool:
        openToClosed = {"(": ")", "{": "}", "[": "]"}
        
        stack = []

        for bracket in s:
            if bracket in openToClosed:
                stack.append(bracket)
            else:
                if not stack or openToClosed[stack[-1]] != bracket:
                    return False
                else:
                    stack.pop()
        
        return not stack