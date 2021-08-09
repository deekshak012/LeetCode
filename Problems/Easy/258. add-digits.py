class Solution(object):
    def addDigits(self, nums):
        while(nums>9):
            sums=0
            while(nums>0):
                sums = sums + nums%10
                nums //=10
            nums=sums
        return nums
        
            
# while num>9:
#     num=sum(int(c) for c in str(num))
# return num
            
            
            
        