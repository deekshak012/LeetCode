class Solution(object):
    def maxProfit(self, prices):
        if len(prices) is 0: return 0
        maxProfit,localmaxprofit,minPrice=0,0,prices[0]      
        for i,price in enumerate(prices):
                if(price<minPrice):
                    minPrice=price
                elif (price>minPrice):
                    maxProfit=maxProfit+price-minPrice
                    if i is not len(prices)-1:
                        minPrice=prices[i+1]
        return maxProfit
    
        