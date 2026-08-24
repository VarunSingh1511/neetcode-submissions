class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(lst):
            if not lst:
                return False
            n = len(lst)
            for i in range(n//2):
                if lst[i] != lst[n-i-1]:
                    return False

            return True

        res = []
        cur = []

        def dfs(i):
            if i == len(s):
                res.append(cur.copy())
                return

            for j in range(i, len(s)):
                substr = s[i:j+1]
                if isPalindrome(substr):
                    cur.append(substr)
                    dfs(j+1)
                    cur.pop()

        dfs(0)
        return res