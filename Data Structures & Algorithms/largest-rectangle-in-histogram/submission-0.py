class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        largest = 0
        for idx,h in enumerate(heights + [0]):
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

        return largest
        