class Solution:
    def isValid(self, s: str) -> bool:
        # should add left bracket without processing and check but when we add right should do processing 
        # we should push and pop successfully and return true but interupt with false if condition breaks  
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif (stack and ((s[i] == ')' and stack[-1] == '(') 
                    or (s[i] == '}' and stack[-1] == '{')
                    or (s[i] == ']' and stack[-1] == '['))):
                    stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
        
