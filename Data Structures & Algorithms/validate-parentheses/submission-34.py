class Solution:
    def isValid(self, s: str) -> bool:
        """
        Brute force: repeatedly strip adjacent matched pairs.

        Key insight: in any valid string, there must exist at least one
        adjacent matching pair "()", "[]", or "{}" somewhere. Remove all
        such pairs, then repeat. If the string ends up empty, it's valid.

        Why this works for ordering: adjacent pairs are, by definition,
        the innermost correctly-nested brackets. Removing them exposes
        the next layer, exactly like unwrapping.
        """
        if not s:               # None or "" -> valid
            return True
        if len(s) % 2 != 0:     # odd length can never be balanced
            return False

        # Keep stripping until no matched adjacent pair remains.
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")

        return s == ""