class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        
        types = {}
        for i in range(len(candies)):
            if candies[i] not in types.keys():
                types[candies[i]] = 1

        return(min(len(types), len(candies)//2) )