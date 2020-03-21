class Solution:
    def titleToNumber(self, s: str) -> int:
        final = 0
        
        level = 0
        for i in range(len(s)-1, -1, -1):
            final += (ord(s[i])-64)*26**level
            level += 1
            
        return final