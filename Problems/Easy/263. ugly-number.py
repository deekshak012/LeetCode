class Solution(object):
    def isUgly(self, n):
        if n<=0:
            return False
        while(n>0):
            if(n==1):
                return True
            elif(n%2==0):
                n=n/2
            elif(n%3==0):
                n=n/3
            elif(n%5==0):
                n=n/5
            else:
                return False
        return True
            