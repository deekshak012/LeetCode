class Solution:
    def countBits(self, n: int) -> List[int]:
        results=[0]
        for i in range(1,n+1):
            results.append(results[i//2]+i%2)
        return results
             
#class Solution:
#     def countBits(self, n: int) -> List[int]:
#         results=[]
#         for i in range(n+1):
#             result=0
#             while(i>0):
#                 if(i%2==1):
#                     result+=1
#                 i//=2
#             results.append(result)
#         return results
                
            
                
            
                