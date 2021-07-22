class Solution(object):
    def isValid(self, s):
        dict = {')':'(','}':'{',']':'['}
        newstr=[]
        for str in s:
            if(str=='('or str=='{'or str=='['):
                newstr.append(str)
            else:
                if(len(newstr)==0 or newstr.pop()!=dict.get(str)):
                    return False
        return newstr==[]
            