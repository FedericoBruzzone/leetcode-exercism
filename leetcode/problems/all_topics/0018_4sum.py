from re import S
from all_import import *

'''
Given an array nums of n integers, return an array of all the unique 
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 
Constraints:
- 1 <= nums.length <= 200
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def kSum( nums: List[int], target: int, k: int) -> List[List[int]]:  
            nums.sort()
            
            res = []
            
            if not nums: return res
            
            average_value = target // k
            if average_value < nums[0] or average_value > nums[-1]:
                return res
            
            if k == 2: return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
            
            return res
        
        def twoSum(nums: List[int], target: int) -> List[List[int]]:  
            #nums.sort()
            
            res = []
            hi = len_s = len(nums) - 1
            lo = 0
            
            while lo < hi:
                current_sum = nums[lo] + nums[hi]
                if current_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif current_sum > target or (hi < len_s and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res
        
        return kSum(nums, target, 4)    