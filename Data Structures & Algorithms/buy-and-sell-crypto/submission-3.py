class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        l,r = 0,0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit<0:
                l=r
            else:
                bestProfit = max(bestProfit,profit)

            r+=1


        return bestProfit