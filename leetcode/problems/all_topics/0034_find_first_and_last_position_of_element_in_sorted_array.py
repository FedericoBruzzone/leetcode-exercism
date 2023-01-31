from all_import import *

'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums is a non-decreasing array.
- -10^9 <= target <= 10^9
'''

class Solution:
    def min(self, nums, target, start, end):
        index = -1
        while start <= end:
            mid = int((start + end) / 2)
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                index = mid
                end = mid - 1
        return index

    def max(self, nums, target, start, end):
        index = -1
        while start <= end:
            mid = int((start + end) / 2)
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                index = mid
                start = mid + 1
        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1

        res = [self.min(nums, target, start, end), \
               self.max(nums, target, start, end)]
        return res
