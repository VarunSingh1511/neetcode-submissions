class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        sumR = 0
        for i in operations:
            if i == '+':
                record.append(int(record[-1]) + int(record[-2]))
            
            elif i == 'D':
                record.append(2 * int(record[-1]))

            elif i == 'C':
                record.pop()

            else:
                record.append(i)
        
        for j in record:
            sumR += int(j)
        return sumR