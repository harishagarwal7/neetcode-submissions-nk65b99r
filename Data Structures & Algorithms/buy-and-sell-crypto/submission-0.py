class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        bp=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if(prices[i]-bp>profit):
                profit=prices[i]-bp
            elif(prices[i]<bp):
                maxProfit=max(maxProfit,profit)
                bp=prices[i]
        maxProfit=max(profit,maxProfit)
        return maxProfit
            
        