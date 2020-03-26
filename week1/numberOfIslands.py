class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#####################################################
        def union(j, k, nodeSets):
            root1 = find(j, nodeSets)
            root2 = find(k, nodeSets)
                
            if root1 != root2:
                nodeSets[root2] = root1
                
            
                
        def find(toLook, nodeSets):
            while toLook != nodeSets[toLook]:
                toLook = nodeSets[toLook]
                find(toLook, nodeSets)
            
            return toLook
######################################################       
        if not grid:
            return 0
        
        result = 0
        nodeSets = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    
                    #if it isnt in nodeSets, create it and add all of its adjacent
                    if (i,j) not in nodeSets.keys():
                        nodeSets[(i,j)] = (i,j)
                            
                    #check left
                    if j-1 >= 0 and grid[i][j-1] == '1':
                        if (i,j-1) not in nodeSets.keys():
                            nodeSets[(i, j-1)] = (i,j-1)
                        union((i,j), (i,j-1), nodeSets)

                        
                    #check right  
                    if j+1 < len(grid[0]) and grid[i][j+1] == '1':
                        if (i,j+1) not in nodeSets.keys():
                            nodeSets[(i, j+1)] = (i,j+1)
                        union((i,j), (i,j+1), nodeSets)


                    #check above
                    if i-1 >= 0 and grid[i-1][j] == '1':
                        if (i-1,j) not in nodeSets.keys():
                            nodeSets[(i-1, j)] = (i-1,j)
                            
                        union((i,j), (i-1,j), nodeSets)


                    #check below
                    if i+1 < len(grid) and grid[i+1][j] == '1':
                        if (i+1,j) not in nodeSets.keys():
                            nodeSets[(i+1, j)] = (i+1,j)
                        union((i,j), (i+1,j), nodeSets)


        for i in nodeSets:
            if i == nodeSets[i]:
                result += 1
                
        return result