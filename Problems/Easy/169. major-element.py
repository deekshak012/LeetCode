class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
        
#considering majority element is less than or more than n/2 times        
# ht={}
# for num in nums:
#     if(not ht.has_key(num)):
#         ht[num]=1
#     else:
#         ht[num]+=1
# maxi=[None,None]
# for key, value in ht.items(): 
#     if value>maxi[1]:
#         maxi=[key,value]
# return maxi[0]