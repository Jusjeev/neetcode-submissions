class Solution:
    def isValid(self, s: str) -> bool: 
        # imporvements - no complicated if else statements, dict for mapping closing bracket with corresponding open bracket!
        # anyways you got the ideal solution idea  
        closeToOpen = {'}' : '{', ']' : '[', ')' : '('}
        stack = []
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if len(stack) == 0:
            return True
        else:
            return False
        
