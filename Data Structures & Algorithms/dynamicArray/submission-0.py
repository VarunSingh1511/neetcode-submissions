class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.length=0
        self.arr=[0]*capacity

    def get(self, i: int) -> int:
        if i<self.length:
            return self.arr[i]
        else:
            return

    def set(self, i: int, n: int) -> None:
        if i<self.length:
            self.arr[i] = n
            return
        else:
            return


    def pushback(self, n: int) -> None:
        if self.length==self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1


    def popback(self) -> int:
        if self.length==0:
            return
        self.length-=1
        n = self.arr[self.length]
        self.arr[self.length]=0
        return n
        

    def resize(self) -> None:
        self.capacity*=2
        tarr=[0]*self.capacity
        for i in range(self.length):
            tarr[i] = self.arr[i]
        self.arr = tarr
    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
