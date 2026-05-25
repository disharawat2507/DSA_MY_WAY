# Leetcode: https://leetcode.com/problems/generate-parentheses/
# Approach : I have used recursion and back tracking to solve this problem. the base case will be when both opening and closing brackets becomes equal to n. 
#now lets start checking open, if open is less than n, we can add open bracket. and get all the combinations with that open bracket.then moving to close bracket, whenever close count is less than open count, we can add
#close brackets. once the base condition is hit, we add the string version in main result and start removing brackets. first all the closing brackets will be removed, then coming to opening brackets,
#we have to remove opening brackets till open becomes less than n, and then again the method will start making other combinations like open = 1 and close =0 so add close brackets and move on.
  
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res =[]       
        getallcombinations(0,0,n,[],res)
        return res
        
def getallcombinations(open, close, n , temp,res):
    if open == n and close == n:
        res.append(''.join(temp))
        return 

    #open
    if open < n:
        temp.append('(')
        getallcombinations(open+1, close, n , temp,res) 
        temp.pop()
            
    #close
    if close < open:
        temp.append(')')
        getallcombinations(open, close+1, n , temp,res) 
        temp.pop()


