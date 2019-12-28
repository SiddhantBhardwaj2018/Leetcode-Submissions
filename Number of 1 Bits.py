
class Solution:
    def hammingWeight(self, string: int) -> int:
        '''
        Problem Description - Write a function that takes an unsigned integer 
        and return the number of '1' bits it has (also known as the Hamming weight).

        Performance - Runtime: 24 ms, faster than 90.51% of Python3 online submissions for Number of 1 Bits.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Number of 1 Bits.
        '''
        return bin(string).count('1')