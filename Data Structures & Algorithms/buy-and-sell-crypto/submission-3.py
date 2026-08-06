# find smalles number, make that keft and start right pointer from there, update left once you find number smaller than left one.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        if len(prices) == 1: return profit
        left=0
        while left< len(prices)-1:
            if prices[left]>prices[left+1]:
                left+=1
            else:
                right = left+1
                while right<len(prices) and prices[left]<prices[right]:
                    profit=max(profit,prices[right]-prices[left])
                    right+=1
                left=right
        return profit

        