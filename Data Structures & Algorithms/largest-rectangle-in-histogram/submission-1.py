class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        largest = 0
        for idx,h in enumerate(heights):
            ##
            flag = 0
            ind = idx
            if stk and stk[-1][0] >= h:
                flag = 1

            while stk and stk[-1][0] > h:
                l,ind = stk.pop()
                area = l * (idx-ind)
                largest = max(largest,area)

            ##
            if flag == 1:
                stk.append((h,ind))

            else:
                stk.append((h,idx))
        
        for h,i in stk:
            largest = max(largest, h * (len(heights)-i))

        return largest
        