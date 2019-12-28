
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        Problem Description - Compute and return the square root of x, where x is guaranteed to be a non-negative integer.Since the return type is an integer,
        the decimal digits are truncated and only the integer part of the result is returned.
        
        Performance - Runtime: 24 ms, faster than 98.43% of Python3 online submissions for Sqrt(x).
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Sqrt(x).
        '''
        return int(math.sqrt(x))