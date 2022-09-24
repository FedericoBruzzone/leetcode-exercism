from all_import import *

'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        for i in range(256): store[i] = -1
            
        len_s = len(s)
        i = max_len = 0
        for j in range(len_s): 
            if store[ord(s[j])] >= i: 
                i = store[ord(s[j])] + 1 # 
            store[ord(s[j])] = j
            max_len = max(max_len, j - i + 1)
        return max_len