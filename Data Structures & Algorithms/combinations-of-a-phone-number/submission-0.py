class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combs = []
        curComb = []

        def dfs(i):
            if i >= len(digits):
                if curComb==[]:
                    return
                combs.append("".join(curComb))
                return
            lst = hm[digits[i]]
            for j in range(0 , len(lst)):
                curComb.append( lst[j] )
                dfs(i+1)
                curComb.pop()

        dfs(0)
        return combs

