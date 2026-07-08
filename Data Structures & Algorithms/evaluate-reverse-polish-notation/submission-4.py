class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i in ['+','-','/','*']:
                a = stk.pop()
                b = stk.pop()
                if i == '+':
                    stk.append(b+a)
                if i == '-':
                    stk.append(b-a)
                if i == '/':
                    stk.append(int(b/a))
                if i == '*':
                    stk.append(b*a)
            else:
                stk.append(int(i))
        res = stk[-1]
        return res