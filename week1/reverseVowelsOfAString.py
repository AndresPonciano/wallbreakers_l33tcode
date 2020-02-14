class Solution:
    def reverseVowels(self, s: str) -> str:
        list1 = []
        for i in range(len(s)):
            if s[i].lower() == 'a' or s[i].lower() == 'e' or s[i].lower() == 'i' or s[i].lower() == 'o' or s[i].lower() == 'u':
                list1.append((s[i], i))
                
        end = len(list1)-1
        s = list(s)
        
        for j in range(int(len(list1)/2)):
            s[list1[j][1]] = list1[end][0]
            s[list1[end][1]] = list1[j][0]
            end -= 1
            
        str = ""
        for ele in s:
            str += ele
        return str