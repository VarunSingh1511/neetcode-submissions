class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxlen = 1
        l = 0
        window = set()
        for r in range(len(s)):
            maxlen = max(maxlen,r-l)

            while s[r] in window:
                window.remove(s[l])
                l+=1


            window.add(s[r])
        
        
        maxlen = max(maxlen, len(s) - l)
        return maxlen
