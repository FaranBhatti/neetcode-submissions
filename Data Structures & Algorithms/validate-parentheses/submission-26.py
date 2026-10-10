class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {')':'(', '}':'{', ']':'['}

        stack = []

        for bracket in s:
            if bracket not in closedToOpen:
                stack.append(bracket)
            else:
                if not stack or stack[-1] != closedToOpen[bracket]:
                    return False
                stack.pop()
        
        return not stack