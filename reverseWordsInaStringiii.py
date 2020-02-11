class Solution:
    def reverseWords(self, s: str) -> str:
        final = ""
        words = s.split()
        for i in range(len(words)):
            for j in range(len(words[i])-1, -1, -1):
                final += words[i][j]
            if i != len(words)-1:
                final += " "

        return final