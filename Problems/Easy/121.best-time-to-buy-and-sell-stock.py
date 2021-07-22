class Solution(object):
    def maxProfit(self, prices):
        if len(prices) is 0: return 0
        maxProfit,minPrice=0,prices[0]      
        for price in prices:
                if(price<minPrice):
                    minPrice=price
                elif (price-minPrice>maxProfit):
                    maxProfit=price-minPrice
        return maxProfit
    
        
            
        