from all_import import *

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.
'''


# Vertical solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or strs == None: return ""
        
        for i in range(len(strs)):
            prefix = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != prefix:
                    return strs[0][0:i]
        return strs[0]

# Divide and Conquer solution
def commonPrefix(left: str, right: str):
    len_min= min(len(left), len(right))
    
    for i in range(len_min):
        if left[i] != right[i]:
            return left[0:i]
    return left[0:len_min]

def longestCommonPrefix(strs: List[str], l: int, r: int) -> str:
        if l == r:  
            return strs[l]
        else:
            mid = l+r//2
            right = longestCommonPrefix(strs, l, mid)
            left = longestCommonPrefix(strs, mid + 1, r)
            return commonPrefix(left, right)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or strs == None: return ""
        return longestCommonPrefix(strs, 0, len(strs) - 1)
        
        
        