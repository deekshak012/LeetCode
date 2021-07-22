class Solution(object):
    def generate(self, numRows):
        if numRows >=1: 
            nums=[[1]]
        if(numRows>=2):
            nums=[[1],[1,1]]
        if(numRows>=3):
            for i in range(2,numRows):
                num=[1]
                for j in range(0,len(nums[i-1])-1):
                    sum = nums[i-1][j]+nums[i-1][j+1]
                    num.append(sum)
                num.append(1)
                nums.append(num)
        return nums
    #Online Solution
    
    # def generate(self, numRows):
    #     res = [[1]]
    #     for i in range(1, numRows):
    #         res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
    #     return res[:numRows]