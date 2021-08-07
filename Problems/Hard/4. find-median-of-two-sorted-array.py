#this wouldnt work since the time complexity is O(m+n)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        arr = []
        while(len(nums1) and len(nums2)):
            if(nums1[0]<nums2[0]):
                arr.append(nums1[0])
                nums1=nums1[1:]
            elif(nums2[0]<nums1[0]):
                arr.append(nums2[0])
                nums2=nums2[1:]
            else:
                arr.append(nums1[0])
                nums1=nums1[1:]
                arr.append(nums2[0])
                nums2=nums2[1:]
        while(len(nums1)):
            arr.append(nums1[0])
            nums1=nums1[1:]
        while(len(nums2)):
            arr.append(nums2[0])
            nums2=nums2[1:]
        c = len(arr)
        if(c%2 != 0):
            return arr[(c-1)/2]
        else:
            return float(arr[c/2 - 1]+arr[c/2])/2
        