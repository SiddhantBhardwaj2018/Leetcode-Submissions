
class Solution(object):
    def removeElement(self, nums, val):
        '''
        Problem Description - Given an array nums and a value val, remove all instances of that value in-place and return the new length.
        
        Performance - Runtime: 20 ms, faster than 65.73% of Python online submissions for Remove Element.
        
        Memory Usage: 11.8 MB, less than 39.62% of Python online submissions for Remove Element.
        '''
        nums[:] = [i for i in nums if i != val]
        return(len(nums))