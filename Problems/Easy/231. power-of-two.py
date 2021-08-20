class Solution(object):
    def isPowerOfTwo(self, n):
        if(n<=0):
            return False;
        return not n&(n-1);
        
#different solution
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         i=1
#         while(i<=n):
#             if(i==n):
#                 return True
#             i=i<<1
#         return False