# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.DFS(root, res)
        return res

    def DFS(self, root, res):
        if not root:
            return
        self.DFS(root.left, res)
        res.append(root.val)
        self.DFS(root.right, res)