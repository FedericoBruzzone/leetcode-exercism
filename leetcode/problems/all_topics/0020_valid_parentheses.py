from all_import import *

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 
Constraints:
- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets_stack = []
        open_brackets = ('(', '[', '{')
        close_brackets = (')', ']', '}')
        
        for curr_elem in s:
            if curr_elem in open_brackets:
                brackets_stack.append(curr_elem)
            else:
                if not brackets_stack == []:
                    last_elem = brackets_stack.pop()
                    if not close_brackets.index(curr_elem) == open_brackets.index(last_elem):
                        return False
                elif brackets_stack == [] and len(s) > 0:
                    return False
                    
        if not brackets_stack == []: return False
        
        return True
