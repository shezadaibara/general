"""
There are two sorted arrays nums1 and nums2 of size m and n respectively. 
Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        sortedLst = sorted(nums2+nums1)
        lstLen = len(sortedLst)
        index = (lstLen - 1) // 2

        if (lstLen % 2):
            return sortedLst[index]
        else:
            return (sortedLst[index] + sortedLst[index + 1])/2.0
    

if __name__ == '__main__':
    nums1 = [1, 3, 5, 6, 7, 8, 10, 12, 25]
    nums2 = [0, 2, 6, 9, 11, 13, 14, 15, 16, 17, 18]
    s = Solution()
    s.findMedianSortedArrays(nums1, nums2)