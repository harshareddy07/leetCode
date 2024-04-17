class Solution(object):
    def isValid(self, s):
        
        stack = []    
        mapByCloseBrackets = {
            ']' : '[',
            '}' : '{',
            ')' : "("
        }


        for c in s:
            if c in mapByCloseBrackets :
                if stack and stack[-1] == mapByCloseBrackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False