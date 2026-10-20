class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sorted_s = Counter(s)
        sorted_t = Counter(t)

        return sorted_s == sorted_t