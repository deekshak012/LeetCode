class Solution(object):
    def isAnagram(self, s, t):
        ht={}
        for c in s:
            if(c in ht):
                ht[c]+=1
            else:
                ht[c]=1
        for c in t:
            if(c in ht):
                ht[c]-=1
            else:
                return False
        for c in ht:
            if(ht[c]!=0):
                return False
        return True
        