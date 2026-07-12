class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxlen = 1
        l = 0
        window = set()
        for r in range(len(s)):


            while s[r] in window:
                maxlen = max(maxlen,r-l)
                window.remove(s[l])
                l+=1


            window.add(s[r])
        
        
        maxlen = max(maxlen, len(s) - l)
        return maxlen
