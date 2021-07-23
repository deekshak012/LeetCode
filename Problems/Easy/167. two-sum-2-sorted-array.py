class Solution(object):
     def twoSum(self, numbers, target):
            for i in xrange(len(numbers)):
                l,r=i+1,len(numbers)-1
                diff = target-numbers[i]
                while(l<=r):
                    mid = (l+r)/2
                    if diff == numbers[mid]:
                        return [i+1,mid+1]
                    elif diff < numbers[mid]:
                        r=mid-1
                    else:
                        l=mid+1

# two-pointer solution
# def twoSum1(self, numbers, target):
#     l, r = 0, len(numbers)-1
#     while l < r:
#         s = numbers[l] + numbers[r]
#         if s == target:
#             return [l+1, r+1]
#         elif s < target:
#             l += 1
#         else:
#             r -= 1




#Recursive method
# class Solution(object):
#     def twoSum(self, numbers, target):
#         maxi=len(numbers)-1
#         for i in xrange(len(numbers)):
#             secondnum = self.binarysearch(numbers,target-numbers[i],i+1,maxi)
#             if secondnum!=-1:
#                 return[i+1,secondnum+1]
            
#     def binarysearch(self, numbers, target, mini, maxi):  
#         if(mini>maxi): return -1
#         mid=(mini+maxi)/2
#         if(target==numbers[mid]):
#             return mid
#         elif(target>numbers[mid]): return self.binarysearch(numbers,target,mid+1,maxi)
#         else:
#             return self.binarysearch(numbers,target,mini,mid-1)