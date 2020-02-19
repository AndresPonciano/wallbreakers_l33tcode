class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        results = collections.Counter()
        answer = []
        for i in range(len(cpdomains)):
            tempList = cpdomains[i].split()
            tempList2 = tempList[1].split('.')
            
            temp = ""
            for j in range(len(tempList2)-1, -1, -1):
                if j != len(tempList2)-1:
                    temp = tempList2[j] + '.' + temp
                else:
                    temp = tempList2[j]
                results[temp] += int(tempList[0])
                
        for i in results:
            answer.append(str(results[i]) + " " + str(i))
            
        return answer