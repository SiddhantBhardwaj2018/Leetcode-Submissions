
def reverse(x):
    '''
    Description of Problem - Given a 32-bit signed integer, reverse digits of an integer.

    Performance - Runtime: 28 ms, faster than 89.61% of Python3 online submissions for Reverse Integer.
    Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Reverse Integer.

    '''
    if x < 0:
        if int('-' + str(x)[1:][::-1]) > -2 ** 31:
            return int('-' + str(x)[1:][::-1])
        return 0
    if x > 0:
        if int(str(x)[::-1]) < (2 ** 31 - 1):
            return int(str(x)[::-1])
        return 0
    if x == 0:
        return 0