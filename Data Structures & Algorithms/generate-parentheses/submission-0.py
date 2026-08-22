class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stk = []

        def backtrack(nopen, nclose):
            if nopen == nclose == n:
                res.append("".join(stk))
                return

            if nopen < n:
                stk.append("(")
                backtrack(nopen + 1, nclose)
                stk.pop()

            if nclose < nopen:
                stk.append(")")
                backtrack(nopen, nclose + 1)
                stk.pop()


        backtrack(0, 0)
        return res