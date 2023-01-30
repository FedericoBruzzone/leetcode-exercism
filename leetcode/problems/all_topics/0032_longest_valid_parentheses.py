from all_import import *

'''
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring
.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
 
Constraints:
- 0 <= s.length <= 3 * 10^4
- s[i] is '(', or ')'.
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        m = 0
        
        for i in range(len(s)):
            print(stack, m)
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    m = max(m, i - stack[-1])
        return m
