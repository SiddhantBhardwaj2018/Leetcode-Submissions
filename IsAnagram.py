
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Problem Description - Given two strings s and t , write a function to determine if t is an anagram of s.
        
        Performance - Runtime: 44 ms, faster than 85.53% of Python3 online submissions for Valid Anagram.
        
        Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Valid Anagram.
        '''
        d1 = {}
        d2 = {}
        for i in s:
            if i not in d1:
                d1[i] = 1
            d1[i] += 1
        for j in t:
            if j not in d2:
                d2[j] = 1
            d2[j] += 1
        return(d1 == d2)