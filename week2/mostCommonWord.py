class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        list1 = paragraph.split()
        counter = collections.Counter()
        
        for i in range(len(list1)):
            temp = list1[i].lower()

            s = ""
            for j in range(len(temp)):
                if temp[j].isalpha():
                    s += temp[j]
                else:
                    counter[s] += 1
                    s = ""
                    
            counter[s] += 1            
                
        for j in counter.most_common():
            if j[0] not in banned and j[0] != '':
                return j[0]