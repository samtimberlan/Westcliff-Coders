# ValaidParentheses

class Solution:
    def isValid(self, s: str) -> bool:
        sLen = len(s)
        # if there is only 1 char, return false
        if sLen < 2:
            return False
        # create a stack
        # use the FILO rule, 
        # match the second half of parentheses with its first half
        sStack = []
        for i in range(sLen):
            currChar = s[i]
            if currChar in ['(', '[', '{']:
                sStack.append(currChar)
            elif currChar in [')', ']', '}']:
                # edge case: if thare only second half, 
                # then the sStack will be empty, will give error when pop
                if len(sStack) == 0:
                    return False
                
                # otherwise, pop a char to match with curr char
                otherHalf = sStack.pop()
                if currChar == ')':
                    if otherHalf != '(':
                        return False
                if currChar == ']':
                    if otherHalf != '[':
                        return False
                if currChar == '}':
                    if otherHalf != '{':
                        return False                        

            else:
                print('unexpected char')
        
        # after matching, the stack should be empty,
        # otherwise return false
        if len(sStack) == 0:
            return True
        else:
            return False


# FirstUniqueCharacterinaString
class Solution:
    def firstUniqChar(self, s: str) -> int:
        sLen = len(s)
        # edge case, if only 1 char, return the char
        if sLen < 2:
            return 0
        # loop through string and convert it to a dictionary
        # use char as key and its count as value
        # loop through the string by pop(0) to find the first char with 1 cnt
        sDic = {}
        for i in range(sLen):
            currChar = s[i]
            if currChar in sDic:
                sDic[currChar] = sDic[currChar] + 1
            else:
                sDic[currChar] = 1
            
        for i in range(sLen):
            currChar = s[i]
            if sDic[currChar] == 1:
                return i

        return -1
