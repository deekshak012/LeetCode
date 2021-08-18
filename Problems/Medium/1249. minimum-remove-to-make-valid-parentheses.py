#goldman sachs
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        s = list(s)
        for i in range(len(s)):
            if(s[i]=='('):
                stack.append(i)
            elif(s[i]==')'):
                if(len(stack)!=0):
                    stack.pop()
                else:
                     s[i]=" "
        for i in stack:
            s[i]=" "
        s = ''.join(s)                    
        s = s.replace(' ', '')
        return s