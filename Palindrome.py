
class Solution(object):
    def isPalindrome(self, x):
        '''
        Description of Problem - Determine whether an integer is a palindrome. An integer is a 
        palindrome when it reads the same backward as forward.
        
        Performance - Runtime: 56 ms, faster than 52.88% of Python online submissions for Palindrome Number.
        
        Memory Usage: 11.6 MB, less than 83.13% of Python online submissions for Palindrome Number.
        
        '''
        if str(x)[0:] == str(x)[::-1]:
            return True
        return False