# Leetcode 17. Letter Combinations of a Phone Number
# Approach : we have to make all combinations of the alphabets of the number mentioned in the form of string. we use backtracking here and add all the combinations.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letterMap = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        backtracking(letterMap,res,0,digits,[])
        return res

def backtracking(letterMap,res,idx,digits,temp):
    if idx == len(digits):
        res.append(''.join(temp))
        return
    choice = letterMap[digits[idx]] # if 2 is at index 0 of digit, then choice will be 'abc'. 

    for i in choice:
        temp.append(i)
        backtracking(letterMap,res,idx+1,digits,temp)
        temp.pop()
    return   
