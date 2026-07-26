class Node:
    def __init__(self,val):
        self.val=val
        self.next = None



class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while i < index and cur:
            cur = cur.next
            i+=1
        if cur==None:
            return -1
        return cur.val

    def insertHead(self, val: int) -> None:
        NewNode = Node(val)
        if not self.head:
            self.head=NewNode
            self.tail=NewNode
            return

        NewNode.next = self.head
        self.head = NewNode

        
    def insertTail(self, val: int) -> None:
        NewNode = Node(val)
        if not self.head:
            self.head=NewNode
            self.tail=NewNode
            return
        
        self.tail.next = NewNode
        self.tail = NewNode

    def remove(self, index: int) -> bool:
        if self.tail == None:
            return False
        if index==0:
            if self.head ==  self.tail:
                self.head=None
                self.tail=None
                return True
            self.head = self.head.next
            return True
        
        cur = self.head
        i = 0
        prev = None
        while i<index and cur:
            prev = cur
            cur = cur.next
            i+=1
        if cur == None:
            return False
        prev.next = cur.next
        if cur==self.tail:
            self.tail = prev
        return True            
        


    def getValues(self) -> List[int]:
        res=[]
        cur=self.head
        while cur:
            res.append(cur.val)
            cur=cur.next
        return res