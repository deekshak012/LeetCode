class Solution(object):
    def maxSubArray(self, nums):
        highestcur = highestoverall = nums[0]
        for i in range(1,len(nums)):
            highestcur = max(nums[i],highestcur+nums[i])
            highestoverall = max(highestoverall,highestcur)
        return highestoverall
        
        