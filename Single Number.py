
class Solution:
    def singleNumber(self, lst: List[int]) -> int:
        '''
        Problem Description - Given a non-empty array of integers, every element appears twice except for one. Find that single one.
        
        Performance - Runtime: 88 ms, faster than 83.04% of Python3 online submissions for Single Number.
        Memory Usage: 15.1 MB, less than 19.67% of Python3 online submissions for Single Number.
        '''
        d = {}
        for i in lst:
            if i not in d:
                d[i] = 0
            d[i] += 1
        for j in d:
            if d[j] == 1:
                return j 