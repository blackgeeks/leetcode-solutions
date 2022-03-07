import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # this is built in use
        # return statistics.median(nums1+nums2)
        sorted_array = sorted(nums1+nums2)
        if len(sorted_array)%2==0:
            
            return ((sorted_array[len(sorted_array)//2 -1] + sorted_array[len(sorted_array)//2 ]) / 2)
        else:
            return sorted_array[len(sorted_array)//2]
            