class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        occurrence = {o: i for i, o in enumerate(S)}
        
        last = 0
        prevLast = 0
        toReturn = []
        for i in range(len(S)):
            if occurrence[S[i]] > last:
                last = occurrence[S[i]]
                
            if i == last:
                toReturn.append(last-prevLast+1)
                prevLast = last+1

        return toReturn