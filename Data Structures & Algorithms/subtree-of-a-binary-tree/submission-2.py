class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkSubtree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and checkSubtree(p.left, q.left) and checkSubtree(p.right, q.right)

        def dfs(root, subroot):
            cur = root
            stack = []
            while cur or stack:
                if cur:
                    stack.append(cur)
                    cur = cur.left
                else:
                    cur = stack.pop()
                    if cur.val == subroot.val:
                        if checkSubtree(cur, subroot):
                            return True
                    cur = cur.right
            return False

        return dfs(root, subRoot)