
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        Problem Description - Given two binary strings, return their sum (also a binary string).The input strings are both non-empty and 
        contains only characters 1 or 0.
        
        Performance - Runtime: 24 ms, faster than 97.71% of Python3 online submissions for Add Binary.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Binary.
        '''
        return bin(int(a,2) + int(b,2))[2:]