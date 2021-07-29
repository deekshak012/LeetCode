class Solution(object):
    def isHappy(self, n):
        ht = set()
        while(n not in ht):
            ht.add(n)
            num=n
            sum=0
            while(num>0):
                x=num%10
                sum=sum+x*x
                num=num//10
            n=sum
        if n==1: 
            return True
        else:
            return False
            
        