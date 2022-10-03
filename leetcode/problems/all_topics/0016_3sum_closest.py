from all_import import *

'''
Given an integer array nums of length n and an integer target, find three 
integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:
- 3 <= nums.length <= 1000
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        len_nums = len(nums)
        m = math.inf
        output = 0
        
        for i in range(len_nums):
            j = i + 1
            k = len_nums - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if abs(target - tmp) < m:
                    m = abs(target - tmp)
                    output = tmp
                elif tmp < target:
                    j += 1
                elif tmp > target:
                    k -= 1
                else: 
                    return target
        return output