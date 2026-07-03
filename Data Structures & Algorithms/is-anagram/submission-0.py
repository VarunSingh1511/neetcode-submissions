class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hasht={}
        for c in s:
            if c in hasht:
                hasht[c] += 1
            else:
                hasht[c]=1
        for c in t:
            if c not in hasht:
                return False
            hasht[c] -= 1
        for i in hasht:
            if hasht[i] != 0:
                return False
        return True
        