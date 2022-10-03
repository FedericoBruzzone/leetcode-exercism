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
    <<<<<<< HEAD
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

# Binary Search solution
def isCommonPrefix(strs: List[str], length: int) -> bool:
    str1 = strs[0][0:length]
    for i in range(1, len(strs)):
        if not strs[i].startswith(str1):
            return False
    return True
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or strs == None: return ""
        
        min_len = 2147483647
        
        for i in range(len(strs)):
            min_len = min(min_len, len(strs[i]))
        
        low = 1
        high = min_len
        
        while low <= high:
            mid = low + high // 2
            if isCommonPrefix(strs, mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return strs[0][0:(low + high) // 2]
=======
        ls = len(strs)
        if ls == 1:
            return strs[0]
        prefix = ''
        pos = 0
        while True:
            try:
                current = strs[0][pos]
            except IndexError:
                break
            index = 1
            while index < ls:
                try:
                    if strs[index][pos] != current:
                        break
                except IndexError:
                    break
                index += 1
            if index == ls:
                prefix = prefix + current
            else:
                break
            pos += 1
        return prefix
>>>>>>> 31aca1c4cb002d730c581943f9c44008816e4408
