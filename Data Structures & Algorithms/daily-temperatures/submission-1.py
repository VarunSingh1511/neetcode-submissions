class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[]
        i=0
        no = len(temperatures)
        while i < no:
            j=i
            n=0
            
            while temperatures[i] >= temperatures[j] and j < no -1:
                j=j+1
            
            if j != no and temperatures[j]>temperatures[i]:
                n = j-i
            output.append(n)
            i+=1
        return output
