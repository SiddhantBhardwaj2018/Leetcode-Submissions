
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Problem  Description - Given a sorted array and a target value,
        return the index if the target is found. If not, return the index 
        where it would be if it were inserted in order.
        
        Performance - Runtime: 48 ms, faster than 88.22% of Python3 online submissions for Search Insert Position.
        Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Search Insert Position.
        '''
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            return sorted(nums).index(target)