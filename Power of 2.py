
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        Problem Description - Given an integer, write a function to determine if it is a power of two.
        
        Performance - Runtime: 28 ms, faster than 83.42% of Python3 online submissions for Power of Two.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Power of Two.
        '''
        if n > 0:
            if bin(n).count('1') == 1:
                return True
            return False
        return False