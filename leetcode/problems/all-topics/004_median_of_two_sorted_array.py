from all_import import *

'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -106 <= nums1[i], nums2[i] <= 106
'''

def merge_two_list(nums1: List[int], nums2: List[int], len_nums1: int, len_nums2: int) -> Tuple[List[int],int]:
    merge_list: List[int] = list()
    p1 = p2 = 0
    while p1 < len_nums1 and p2 < len_nums2:
        if nums1[p1] < nums2[p2]:
            merge_list.append(nums1[p1])
            p1 += 1
        else: 
            merge_list.append(nums2[p2])
            p2 += 1
            
    while p1 < len_nums1:
        merge_list.append(nums1[p1])
        p1 += 1
        
    while p2 < len_nums2:
        merge_list.append(nums2[p2])
        p2 += 1
    
    return merge_list, len(merge_list)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if len_nums1 < len_nums2:
            return self.findMedianSortedArrays(nums2, nums1)
        merge_list, len_merge_list = merge_two_list(nums1, nums2, len_nums1, len_nums2)
        
        len_merge_list_div2 = len_merge_list//2
        return merge_list[len_merge_list_div2] \
               if len_merge_list % 2 == 1 \
               else (merge_list[len_merge_list_div2-1] + merge_list[len_merge_list_div2]) / 2