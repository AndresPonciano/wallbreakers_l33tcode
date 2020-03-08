class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        print(s, p)
        
        template, list1 = [0]*26, [0]*26
        
        for i in range(len(p)):
            template[ord(p[i])-97] += 1
            
        
        count = 0
        toReturn = []
        for j in range(len(s)):
            if count < len(p):
                list1[ord(s[j])-97] += 1
                count += 1                

            if count == len(p):
                if list1 == template:
                    toReturn.append(0)
                count += 1
            elif count > len(p):
                list1[ord(s[j])-97] += 1
                list1[ord(s[j-len(p)])-97] -= 1
                
                if list1 == template:
                    toReturn.append(j-len(p)+1)
                
                
        return toReturn