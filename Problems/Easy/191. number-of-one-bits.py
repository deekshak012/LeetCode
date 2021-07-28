class Solution(object):
    def hammingWeight(self, n):
        ans = 0
        for i in xrange(32):
            if(n & 1):
                ans+=1
            n >>= 1
        return ans
        