class Solution(object):
    def reverse(self, x):
        sign = [1,-1][x < 0]
        x=abs(x)
        rev=0
        while(x!=0):
            rev=rev*10+x%10
            x=x/10
        if rev > 2**31+1 or rev < -2**31-1:
            return 0
        return sign*rev