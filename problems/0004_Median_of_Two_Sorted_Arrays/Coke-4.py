# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(nums1 == None and nums2 == None):
            return 0
        nums3 = nums1 + nums2
        nums3.sort()
        n=len(nums3)
        if(n%2==0):
            return float(( nums3[int(n/2)-1] + nums3[int(n/2)] )/2)
        else:
            return float(nums3[int(n/2)])