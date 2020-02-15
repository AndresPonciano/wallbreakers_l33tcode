class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        def find(toLook, nodeSets):
            while(toLook != nodeSets[toLook]):
                toLook = nodeSets[toLook]
                find(toLook, nodeSets)
            
            return toLook
            
            
        def union(j, k, nodeSets):
            root1 = find(j, nodeSets)
            root2 = find(k, nodeSets)
            
            if(root1 != root2):
                nodeSets[root2] = root1
            
            # print(root1)
            # print(root2)
                            
            
        nodeSets = {}
        for i in range(len(M)):
            nodeSets[i] = i
            
        # print(nodeSets)
        
        for j in range(len(M)):
            for k in range(len(M[j])):
                if(M[j][k] == 1 and j != k):
                    # print("---")
                    # print(j, k)
                    union(j, k, nodeSets)
                    # print(nodeSets)
                                    
        # print(nodeSets)
        
        results = set()
        
        for i in range(len(nodeSets)):
            results.add(find(i, nodeSets))
            # print(find(i, nodeSets))
            
        # print(results)
                
        return(len(results))