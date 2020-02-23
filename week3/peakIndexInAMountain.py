class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        start, end = 0, len(A)-1
        mid = (end + start)//2
        
        while start <= end:
            mid = (end + start)//2 
        
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
                start = mid + 1
            elif A[mid] < A[mid-1] and A[mid] > A[mid+1]:
                end = mid - 1