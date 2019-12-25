
class Solution(object):
    def plusOne(self, digits):
        '''
        Problem Description - Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
        
        Performance - Runtime: 12 ms, faster than 97.04% of Python online submissions for Plus One.
        
        Memory Usage: 11.8 MB, less than 16.67% of Python online submissions for Plus One.
        '''
        x = ''
        for element in digits[::]:
            x += str(element)
            y = str(int(x) + 1)
        return([char for char in y])