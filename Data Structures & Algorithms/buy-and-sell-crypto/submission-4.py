# find smallest number, make that keft and start right pointer from there, update left once you find number smaller than left one.

# 2nd: track minimum so far at each index find max profit as you go, update mini alongside
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Not using while loop
        min_so_far = float('inf')
        profit=0
        for price in prices:
            if price<min_so_far:
                min_so_far=price
            else:
                profit=max(profit,price-min_so_far)
        return profit
        # profit=0
        # left=0
        # while left< len(prices)-1:
        #     if prices[left]>prices[left+1]:
        #         left+=1
        #     else:
        #         right = left+1
        #         while right<len(prices) and prices[left]<prices[right]:
        #             profit=max(profit,prices[right]-prices[left])
        #             right+=1
        #         left=right
        # return profit
        
        