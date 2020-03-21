class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 or not s:
            return True
        
        s = (''.join(e for e in s if e.isalnum())).lower()
        
        if s == s[::-1]:
            return True