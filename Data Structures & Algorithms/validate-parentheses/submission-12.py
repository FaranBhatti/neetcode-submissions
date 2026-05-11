class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')': '(', ']': '[', '}': '{'}
        stack = []

        for bracket in s:
            if bracket in close_to_open.values():
                stack.append(bracket)
            elif stack and close_to_open[bracket] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not stack
