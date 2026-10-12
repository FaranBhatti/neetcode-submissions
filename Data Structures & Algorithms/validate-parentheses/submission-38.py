class Solution:
    def isValid(self, s: str) -> bool:
        if not s:           # empty string is valid
            return True
        
        if len(s) % 2 != 0: # odd length can never be balanced
            return False

        while ("()") in s or ("[]") in s or ("{}") in s:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")

        return s == ""