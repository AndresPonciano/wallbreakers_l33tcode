class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = True if sorted(s) == sorted(t) else False
        return result