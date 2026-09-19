
#            i 
#  0 1 2 3 4 5 
#  [10,8,7,5,2]

# minProfitSeenSoFar = 2
# maxProfitAcheived = 0 (difference between current, and minProfit)


# choose to buy on one day and sell on the other day
# return max profit acheived. 

# min amount to buy a stock 
# max amount to sell a stock 

# minSeenSoFar
# maxSeenSoFar 
# maxProfitSeenSoFar 

import sys 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_stock_seen_so_far = sys.maxsize
        max_profit_acheived = 0 

        for price in prices: 
            min_stock_seen_so_far = min(min_stock_seen_so_far, price)
            max_profit_acheived = max(max_profit_acheived, price - min_stock_seen_so_far)
        
        return max_profit_acheived 


     
        