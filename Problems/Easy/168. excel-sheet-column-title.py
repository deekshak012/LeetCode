class Solution(object):
    def convertToTitle(self, num):
        result = ''
        while num > 0:
            result = chr((num-1)%26+65)+result
            num = (num-1) // 26
        return result
        