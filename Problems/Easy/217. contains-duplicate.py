class Solution(object):
    def containsDuplicate(self, nums):
        h={}
        for n in nums:
            if n in h:
                return True
            else:
                h[n]=n
        return False
        
        