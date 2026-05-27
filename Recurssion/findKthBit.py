Approach : used recurssion for solving this question. It is given that for n =1 , the function must return 0, then for next results , function should return the value of n-1 +'1'+reverse(invert(n-1).
 reverse should fully reverse the answer and invert should invert the values in its place. '0' should be '1' and vice versa.                                                                                                                                                                                         
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        memo ={}
        val = findreveresed(n,memo)
        return val[k-1]

def findreveresed(n,memo):
    if n == 1:
        return '0'
    if n in memo:
        return memo[n]  
    val = findreveresed(n-1,memo)      
    v = val +'1' 
    r = invertfunc(val)
    memo[n] = v + r[::-1]
    return  memo[n]   

def invertfunc(n):
    res = ''
    for i in range(len(n)):
        if n[i] =='0':
            res +='1'
        else:
            res +='0'    
    return res        
