class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []
        
        dict1 = {}
        for i in  range(len(nums1)):
            if nums1[i] not in dict1.keys():
                dict1[nums1[i]] = nums1[i]
        
        results = []
        for j in range(len(nums2)):
            if nums2[j] in dict1.keys() and nums2[j] not in results:
                results.append(nums2[j])
                
                
        return(results)