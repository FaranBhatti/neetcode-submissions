class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for bracket in s:
            if bracket in bracket_pairs:
                stack.append(bracket)
            else:
                if stack and bracket_pairs[stack[-1]] == bracket:
                    stack.pop()
                else:
                    return False
        
        return not stack