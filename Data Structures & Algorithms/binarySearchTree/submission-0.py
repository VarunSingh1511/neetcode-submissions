class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
            return
        curr = self.root
        prev = None
        while curr:
            prev = curr
            if key > curr.key:
                curr = curr.right
            elif key < curr.key:
                curr = curr.left
            else:
                curr.val = val
                return
        
        if key > prev.key:
            prev.right = TreeNode(key, val)
        else:
            prev.left = TreeNode(key, val)

        

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key > curr.key:
                curr = curr.right
            elif key < curr.key:
                curr = curr.left
            else:
                return curr.val

        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr.left:
            curr = curr.left

        return curr.val


    def getMax(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr.right:
            curr = curr.right

        return curr.val


    def remove(self, key: int) -> None:
        def deleteNode(root, key):
            if not root:
                return None
            if key < root.key:
                root.left = deleteNode(root.left, key)
            elif key > root.key:
                root.right = deleteNode(root.right, key)
            else:
                if not root.left: return root.right
                if not root.right: return root.left
                
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.key, root.val = temp.key, temp.val
                root.right = deleteNode(root.right, temp.key)
            return root
        self.root = deleteNode(self.root, key)


    def getInorderKeys(self) -> List[int]:
        lst = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            lst.append(root.key)
            dfs(root.right)
        
        dfs(self.root)
        return lst
