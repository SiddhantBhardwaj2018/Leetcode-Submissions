
class Solution:
    def trailingZeroes(self, x: int) -> int:
        '''
        Problem Description - Given an integer n, return the number of trailing zeroes in n!.

        Performance - Runtime: 24 ms, faster than 94.21% of Python3 online submissions for Factorial Trailing Zeroes.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Factorial Trailing Zeroes.
        '''
        power = 1
        count = 0
        while x // (5 ** power) != 0:
            count += x // (5 ** power)
            power += 1
        return count