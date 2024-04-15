class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r = 0,1
        maxProft = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProft = max(profit, maxProft)
            else:
                l = r
            r += 1

        return maxProft 