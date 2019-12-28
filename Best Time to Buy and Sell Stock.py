
class Solution:
    def maxProfit(self, lst: List[int]) -> int:
        '''
        Problem Description - Say you have an array for which the ith element is the price of a given stock on day i.If you were only 
        permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
        design an algorithm to find the maximum profit. Note that you cannot sell a stock before you buy one.
        
        Performance - Runtime: 64 ms, faster than 80.45% of Python3 online submissions for Best Time to Buy and Sell Stock.
        Memory Usage: 13.9 MB, less than 80.46% of Python3 online submissions for Best Time to Buy and Sell Stock.
        '''
        if len(lst) > 0:
            max_prof = 0
            min_price = lst[0]
            for i in lst:
                min_price = min(min_price,i)
                profit = i - min_price
                max_prof = max(max_prof,profit)
            return max_prof
        return 0