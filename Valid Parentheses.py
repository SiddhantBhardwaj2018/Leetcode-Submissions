
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Problem Description - Given a string containing just the characters 
        '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        
        Performance - Runtime: 24 ms, faster than 94.83% of Python3 online submissions for Valid Parentheses.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
        '''
        open1 = ["[","{","("]
        close1 = ["]","}",")"]
        stack = []
        for i in s:
            if i in open1:
                stack.append(i)
            else:
                if len(stack) != 0 and stack[-1] == open1[close1.index(i)]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False