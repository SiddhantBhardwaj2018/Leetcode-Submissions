
class Solution:
    def moveZeroes(self, lst: List[int]) -> None:
        '''
        Problem Description - Given an array nums, write a function to move all 0's to the end of it while 
        maintaining the relative order of the non-zero elements.

        Performance - Runtime: 48 ms, faster than 88.06% of Python3 online submissions for Move Zeroes.
        Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Move Zeroes.
        '''
        count = 0
        for i in range(len(lst)):
            if lst[i] != 0:
                lst[count],lst[i] =  lst[i],lst[count]
                count += 1
        return lst