class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        h={}
        for i,n in enumerate(nums):
            if n in h and abs(h.get(n)-i) <= k:
                return True
            h[n]=i
        return False
        