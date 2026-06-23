### so max profit = highest numer - lowest number
## cant be sorted since O(n) wanted 
## GREEDY: get rid of choices that could never improve
## so right number needs to always be greater, so right > left 
###but when to move left (when small?) and when to move right(when big??)
## BUY HAPPENS BEFORE SELL


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 #buy
        right = 1 #sell
        profit = 0
        max_profit = 0
        lowest_buy = prices[0]

        while right < len(prices): ### selling point less than number of prices 
            profit = prices[right] - prices[left]
            if profit >= 0: ## profit is either 0 or positive
                if max_profit < profit: ## found new bigger profit!
                    max_profit = profit
                ## max_profit > profit so only iterate sell day
                right += 1
            else: ### if profit negative, MUST move buy day
                left = right ### GREEDY ALGGGGGGGG
        return max_profit
            


### ex: left = 10, right = 1 -> 1 < 10 so move 

        