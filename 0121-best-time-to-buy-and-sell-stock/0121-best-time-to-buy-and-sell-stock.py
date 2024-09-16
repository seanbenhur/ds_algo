class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = float('inf'), 0

        for p in prices:
            buy, sell = min(buy,p), max(sell,p-buy)
        return sell

    