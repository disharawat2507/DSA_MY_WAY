# Leetcode 39. Combination Sum
# Approach : used backtracking approach to check sum.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        backtrackingmethod(candidates, target, 0,[],res,0)
        return res 

def backtrackingmethod(candidates, target,idx, temp,res,sumn):

    if sumn == target:
        res.append(temp.copy()) 
        return 
    if sumn > target or idx >= len(candidates):
        return     
    

    temp.append(candidates[idx])
    sumn += candidates[idx]
    backtrackingmethod(candidates, target,idx, temp,res,sumn)
    val = temp.pop()
    sumn -= val

    backtrackingmethod(candidates, target,idx+1, temp,res,sumn)    
        

