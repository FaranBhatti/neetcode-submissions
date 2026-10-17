class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {')': '(', '}': '{', ']':'['}
        stack = []

        for bracket in s:
            if bracket in closedToOpen and stack:
                if closedToOpen[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return not stack