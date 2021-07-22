class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i,num in enumerate(nums):
            if((target-num) in dict):
                return([dict.get(target-num),i])
            else:
                dict[num]=i
                