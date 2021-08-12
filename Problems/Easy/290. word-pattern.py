class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        st= s.split(' ')
        if(len(pattern)!=len(st)):
            return False
        ht={}
        stl={}
        for i in range(len(pattern)):
            if(pattern[i] not in ht and st[i] not in stl):
                ht[pattern[i]]=st[i]
                stl[st[i]]=pattern[i]
            elif(pattern[i] not in ht or st[i] not in stl):
                return False
            elif(ht[pattern[i]]!=st[i] and stl[st[i]]!=pattern[i]):
                return False
        return True
        