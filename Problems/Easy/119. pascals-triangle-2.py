class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex >=0: 
            nums=[[1]]
        if(rowIndex>=1):
            nums=[[1],[1,1]]
        if(rowIndex>=2):
            for i in range(2,rowIndex+1):
                num=[1]
                for j in range(0,len(nums[i-1])-1):
                    sum = nums[i-1][j]+nums[i-1][j+1]
                    num.append(sum)
                num.append(1)
                nums.append(num)
        return nums[rowIndex]
    
    # row = [1]
    #     for _ in range(rowIndex):
    #         row = [x + y for x, y in zip([0]+row, row+[0])]
    #     return row