
class Solution:
    def containsDuplicate(self, lst: List[int]) -> bool:
        '''
        Problem Description - Given an array of integers, find if the array contains any duplicates.
        Your function should return true if any value appears at least twice in the array, 
        and it should return false if every element is distinct.
        
        Performance - Runtime: 120 ms, faster than 96.90% of Python3 online submissions for Contains Duplicate.
        Memory Usage: 18.1 MB, less than 88.68% of Python3 online submissions for Contains Duplicate.
        '''
        if len(lst) == len(set(lst)):
            return False
        return True