
class Solution:
    def majorityElement(self, lst: List[int]) -> int:
        '''
        Problem Description - Given an array of size n, find the majority element. 
        The majority element is the element that appears more than n/2  times.
        
        Performance - Runtime: 164 ms, faster than 99.11% of Python3 online submissions for Majority Element.
        Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Majority Element.
        '''
        d = {}
        for i in lst:
            if i not in d:
                d[i] = 0
            d[i] += 1
        for i in d:
            if d[i] > int(len(lst) / 2):
                return i