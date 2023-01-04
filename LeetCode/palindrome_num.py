# Solved without converting the integer to a string.
# Time complexity: O(n)
# Space complexity: O(1)
from math import log10

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 1: # ignore negatives
            return x == 0 # special case 0 for log10
        
        left = int(log10(x)) # get number of zeroes

        while x > 9: # while x has more than one digit
            l_exp = pow(10, left)
            l_num = x // l_exp
            r_num = x % 10

            if l_num != r_num:
                return False
            
            # remove a zero on both corners
            x -= l_exp * l_num
            x //= 10

            # move pointer
            left -= 2
        
        return (left == 0 and x < 10) or x == 0
