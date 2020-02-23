class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        
        prev = -1
        count = 0
        for i in range(len(points)):
            if prev < 0:
                prev = points[i][1]
                count += 1
            elif prev < points[i][0] or prev > points[i][1]:
                prev = points[i][1]
                count += 1
                
        return count