class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        results = {}
        
        missing = -1
        repeated = -1
        for i in range(len(nums)):
            if nums[i] not in results.keys():
                results[nums[i]] = i
            else:
                repeated = nums[i]
                
            if i+1 not in results.keys():
                missing = i+1
                
        return [repeated, missing]