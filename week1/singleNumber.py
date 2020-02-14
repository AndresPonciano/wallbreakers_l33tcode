class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1 = {}
        
        for i in range(len(nums)):
            if nums[i] not in dict1.keys():
                dict1[nums[i]] = 1
            else:
                del dict1[nums[i]]
            
        return(next(iter(dict1)))