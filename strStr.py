
class Solution(object):
    def strStr(self, haystack, needle):
        """
        Problem Description - Implement strStr(). Return the index of the first occurrence of needle in haystack, or -1 if
        needle is not part of haystack.
        
        Performance - Runtime: 28 ms, faster than 88.00% of Python3 online submissions for Implement strStr().
        
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Implement strStr().
        """
        if needle != "":
            if needle in haystack:
                return(haystack.index(needle))
            return(-1)
        return(0)