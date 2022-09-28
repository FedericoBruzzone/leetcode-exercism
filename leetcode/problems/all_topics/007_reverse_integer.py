from all_import import *

'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
-231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        res, isPos = 0, 1
        if x < 0:
            isPos = -1
            x = -1 * x
        while x != 0:
            pop = x % 10
            x //= 10
            if res > INT_MAX // 10 or (res == INT_MAX and pop > 7): return 0
            if res < INT_MIN // 10 or (res == INT_MIN and pop < -8): return 0
            res = res * 10 + pop
        return res * isPos