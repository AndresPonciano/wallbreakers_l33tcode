class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps = []
        for i in range(len(word)): 
            if word[i].isupper():
                caps.append(word[i])
        
        if not caps:
            return True
        
        if len(word) == len(caps):
            return True
        elif word[0] == caps[0] and len(caps) == 1:
            return True
        else:
            return False