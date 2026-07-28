class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
        


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while i<index and cur:
            cur = cur.next
            i += 1
        if not cur:
            return -1
        return cur.val            

    def addAtHead(self, val: int) -> None:
        cur = Node(val)
        if self.head==None:
            self.head=cur
            self.tail=cur
            return
        cur.next = self.head
        self.head.prev = cur
        self.head = cur

        

    def addAtTail(self, val: int) -> None:
        cur = Node(val)
        if self.tail==None:
            self.head=cur
            self.tail=cur
            return
            
        cur.prev = self.tail
        self.tail.next = cur
        self.tail = cur

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        newnode = Node(val)
        i = 0
        while i<index and cur:
            cur = cur.next
            i += 1
        if not cur:
            if i==index:
                self.addAtTail(val)
            return
        newnode.next = cur
        newnode.prev = cur.prev
        cur.prev.next = newnode
        cur.prev = newnode

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index==0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return
        cur = self.head
        i = 0
        while i<index and cur:
            cur = cur.next
            i += 1
        if not cur:
            return
        if cur.prev:
            cur.prev.next = cur.next
        if cur.next:
            cur.next.prev = cur.prev
        else:
            self.tail = cur.prev