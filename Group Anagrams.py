
class Solution:
    def groupAnagrams(self, lst: List[str]) -> List[List[str]]:
        '''
        Problem Description - Given an array of strings, group anagrams together.
        
        Performance - Runtime: 96 ms, faster than 93.78% of Python3 online submissions for Group Anagrams.
        
        Memory Usage: 16 MB, less than 60.38% of Python3 online submissions for Group Anagrams.
        '''
        d = {}
        for i in lst:
            k = "".join(sorted(i))
            if k not in d:
                d[k] = [i]
            else:
                d[k].append(i)
        return(d.values())