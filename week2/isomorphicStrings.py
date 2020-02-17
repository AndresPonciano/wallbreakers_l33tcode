class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        for i in range(len(s)):
            if s[i] not in dict1.keys() and t[i] not in dict1.values():
                dict1[s[i]] = t[i]
            else:
                if s[i] in dict1.keys():
                    if dict1[s[i]] != t[i]:
                        return False
                elif s[i] in dict1.values():
                    if t[i] not in dict1.keys() or dict1[t[i]] != s[i]:
                        return False
                
                if t[i] in dict1.keys():
                    if dict1[t[i]] != s[i]:
                        return False
                elif t[i] in dict1.values():
                    if s[i] not in dict1.keys() or dict1[s[i]] != t[i]:
                        return False

        
        return True