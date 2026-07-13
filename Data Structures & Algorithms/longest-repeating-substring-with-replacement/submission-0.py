class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen=0
        l=0
        hm = {}

        for r in range(len(s)):
            if s[r] not in hm:
                hm[s[r]]=1
            else:
                hm[s[r]] += 1
        
            while r-l+1 - max(hm.values()) > k:
                hm[s[l]]-=1
                l+=1
            
            maxlen = max(maxlen, r - l + 1)
        return maxlen