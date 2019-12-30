
class Solution:
    def removeDuplicates(self, lst: List[int]) -> int:
        '''
        Problem Description - Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        
        Performance - Runtime: 80 ms, faster than 95.30% of Python3 online submissions for Remove Duplicates from Sorted Array.
        Memory Usage: 14.5 MB, less than 97.54% of Python3 online submissions for Remove Duplicates from Sorted Array.
        '''
        j = 1
        for i in range(len(lst)-1):
            if (lst[i] != lst[i + 1]):
                lst[j] = lst[i + 1]
                j += 1
                
        return j