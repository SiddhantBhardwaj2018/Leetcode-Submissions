
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Description of Problem - Given an array of integers, return indices of the 
        two numbers such that they add up to a specific target.
        
        Runtime: 4596 ms, faster than 23.79% of Python3 online submissions for Two Sum.
        
        Memory Usage: 12.6 MB, less than 75.68% of Python online submissions for Two Summ
        '''
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return([i,j])