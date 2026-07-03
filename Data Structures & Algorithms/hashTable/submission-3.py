class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.table = [None]*capacity
        self.length = 0

    def insert(self, key: int, value: int) -> None:
        idx = key%(self.capacity)
        curr = self.table[idx]
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next
        
        new_node = Node(key, value)
        new_node.next = self.table[idx]
        self.table[idx] = new_node
        self.length += 1
        if self.length >= (self.capacity)/2:
            self.resize()

    def get(self, key: int) -> int:
        idx = key%(self.capacity)
        curr = self.table[idx]
        while curr!=None:
            if curr.key==key:
                return curr.value
            curr = curr.next
        return -1


    def remove(self, key: int) -> bool:
        idx = key%(self.capacity)
        curr = self.table[idx]
        prev = None
        while curr!=None:
            if curr.key==key:
                if prev == None:
                    self.table[idx] = self.table[idx].next
                else:
                    prev.next = curr.next
                self.length -= 1
                return True
            prev = curr
            curr = curr.next
        return False

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.length = 0
        for node in old_table:
            curr = node
            while curr:
                self.insert(curr.key, curr.value)
                curr = curr.next