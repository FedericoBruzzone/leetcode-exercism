from all_import import *

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
- 1 <= n <= 8
'''

# Backtracking solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2*n:
                output.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
            
        output = []
        backtrack()
        return output

# Recursive solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(X = []):
            if len(X) == 2*n:
                if valid(X):
                    output.append("".join(X))
            else:
                X.append('(')
                generate(X)
                X.pop()
                X.append(')')
                generate(X)
                X.pop()
                
        def valid(X):
            bal = 0
            for c in X:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0
            
        output = []
        generate()
        return output