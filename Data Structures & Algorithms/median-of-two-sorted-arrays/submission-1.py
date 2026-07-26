class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        total = len(nums1) + len(nums2)
        half = total//2
        if len(nums1) > len(nums2):
            A,B = B,A
        
        l,r = 0,len(A) - 1

        while True:
            ma = (l+r)//2
            mb = half - ma - 2
            
            AL = A[ma] if ma>=0 else float('-infinity')
            AR = A[ma+1] if (ma+1) < len(A) else float('infinity') 
            BL = B[mb] if mb>=0 else float('-infinity')
            BR = B[mb+1] if (mb+1) < len(B) else float('infinity')

            if AL <= BR and BL <= AR:

                if total%2:
                    return min(AR,BR)
                return  ( min(AR,BR) + max(AL,BL) )/2

            elif AL>BR:
                r = ma-1
            else:
                l = ma+1
                

        
