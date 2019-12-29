
class Solution:
    def sortedSquares(self, lst: List[int]) -> List[int]:
        '''
        Problem Description - Given an array of integers A sorted in non-decreasing order,
        return an array of the squares of each number, also in sorted non-decreasing order.
        
        Performance - Runtime: 232 ms, faster than 88.92% of Python3 online submissions for Squares of a Sorted Array.
        Memory Usage: 14.6 MB, less than 97.62% of Python3 online submissions for Squares of a Sorted Array.
        '''
        lst1 = []
        for i in lst:
            lst1.append(i**2)
        return sorted(lst1)