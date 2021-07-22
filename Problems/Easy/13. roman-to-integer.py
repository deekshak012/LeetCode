class Solution(object):
    def romanToInt(self, s):
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        intval=0
        for i in range(0, len(s)-1):
            if(dict.get(s[i])>=dict.get(s[i+1])):
                intval=intval+dict.get(s[i])
            else:
                intval=intval-dict.get(s[i])
        return intval+dict.get(s[len(s)-1])