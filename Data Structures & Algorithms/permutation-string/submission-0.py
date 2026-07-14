class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm1={}
        hm2={}
        for i in s1:
            hm1[i] = 1 + hm1.get(i,0)
        n = len(s1)
        l,r = 0,0
        while r < len(s2):
            hm2[s2[r]] = 1 + hm2.get(s2[r],0)
            if r-l+1 > n:
                if hm2[s2[l]] == 1:
                    del hm2[s2[l]]
                else:
                    hm2[s2[l]]-=1
                l+=1
            if hm1 == hm2:
                return True

            r+=1

        return False