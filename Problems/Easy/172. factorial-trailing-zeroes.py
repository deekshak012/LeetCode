class Solution(object):
    def trailingZeroes(self, n):
        count=0
        while (n != 0):
            tmp = n / 5
            count += tmp
            n = tmp
        return count
       