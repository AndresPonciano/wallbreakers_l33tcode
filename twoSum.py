class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicta = {}
        for i in range(len(nums)):
            if nums[i] in dicta.keys():
                return(i, dicta[nums[i]]) 
            
            temp = target - nums[i]
            dicta[temp] = i