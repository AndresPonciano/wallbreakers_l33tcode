class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        
        list1 = A.split()
        list2 = B.split()
        
        results = []
        track = {}
        for i in range(len(list1)):
            if list1[i] not in track.keys():
                track[list1[i]] = 1
            else:
                track[list1[i]] += 1
            

        for j in range(len(list2)):
            if list2[j] not in track.keys():
                track[list2[j]] = 1
            else:
                track[list2[j]] += 1
            
        
        for k in track:
            if track[k] == 1:
                results.append(k)
            
        return(results)