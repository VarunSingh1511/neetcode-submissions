class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0]*n
        stk = []
        for i,t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                stkT,stkI = stk.pop()
                output[stkI] = i - stkI

            stk.append((t,i))
        
        return output
