class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        self.homepage.next = None
        self.homepage.prev = None
        self.cur = self.homepage

    def visit(self, url: str) -> None:
        Newnode = Node(url)
        self.cur.next = Newnode
        Newnode.prev = self.cur
        self.cur = Newnode


    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.cur != self.homepage:
            self.cur = self.cur.prev
            i+=1
        return self.cur.val

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.cur.next:
            self.cur = self.cur.next
            i+=1
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)