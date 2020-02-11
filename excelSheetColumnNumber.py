class Solution:
    def titleToNumber(self, s: str) -> int:
        # values = {"A": 1, "B": 2, "C": 3, "D": 4"E": 1, "F": 2, "C": 3, "D": 4}
        # print(values)
        final = 0
        for i in range(len(s)-1, -1, -1):
            print(s[i])
            # final 
            print(((ord(s[i])-64)+(ord("Z")-64)**i)-1)
            final += ((ord(s[i])-64)+(ord("Z")-64)**i)-1
            # final += ((ord("Z")-64)*i)+(ord(s[i])-64)
        
        return final