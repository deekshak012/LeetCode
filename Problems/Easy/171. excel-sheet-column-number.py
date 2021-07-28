class Solution(object):
    def titleToNumber(self, columnTitle):
        num=1/26
        while(len(columnTitle)!=0):
            num=num*26+(ord(columnTitle[0])-64)
            columnTitle=columnTitle[1:]
        return num