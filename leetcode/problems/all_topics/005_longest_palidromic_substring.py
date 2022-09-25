from all_import import *

'''
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters.
'''
def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1 
        right += 1 
    return s[left+1:right]

class Solution: 
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        longest = "" 
        for i in range(len(s)):
            tmp = expandAroundCenter(s, i, i) 
            if len(tmp) > len(longest):
                longest = tmp 

            tmp = expandAroundCenter(s, i, i+1)
            if len(tmp) > len(longest):
                longest = tmp
            
        return longest

    if __name__ == "__main__":
        print(longestPalindrome(None, "abcba"))