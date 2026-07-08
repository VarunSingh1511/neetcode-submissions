class Solution:
    def isValid(self, s: str) -> bool:
        stk =[]

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stk.append(i)
            elif i == ')' or i == '}' or i == ']':
                
                if stk:
                    b = stk.pop()
                else:
                    return False
                if i == ')' and b != '(':
                    return False
                if i == '}' and b != '{':
                    return False
                if i == ']' and b != '[':
                    return False

        if stk:
            return False

        return True