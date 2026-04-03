class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            print(i)
            j=i+1
            for j in range(i+1, len(prices)):
                print(j)
                if(prices[j]-prices[i]>profit):
                    profit=prices[j]-prices[i]
                    print(profit)
        return profit
        