class MinStack:

    def __init__(self):
        self.mstk=[]

    def push(self, val: int) -> None:
        self.mstk.append(val)

    def pop(self) -> None:
        self.mstk.pop()
        

    def top(self) -> int:
        return self.mstk[-1]

    def getMin(self) -> int:
        minE = self.mstk[-1]
        for i in self.mstk:
            if i < minE:
                minE = i
        return minE
        
