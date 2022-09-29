from ssl import HAS_NEVER_CHECK_COMMON_NAME
from all_import import *

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): return False

        revertNumber: int = 0
        while x > revertNumber:
            revertNumber = revertNumber * 10 + x % 10 
            x //= 10

        return x == revertNumber or x == revertNumber // 10

    if __name__ == "__main__":
        print(isPalindrome(None, 101))