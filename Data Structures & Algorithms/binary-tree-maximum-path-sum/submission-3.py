# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = root.val
        def dfs(root):
            if not root:
                return 0
            leftContri = dfs(root.left)
            rightContri = dfs(root.right)
            if leftContri > 0 and rightContri > 0:
                self.maxPath = max(self.maxPath, root.val + leftContri + rightContri)
            elif leftContri > 0 and rightContri <= 0:
                self.maxPath = max(self.maxPath, root.val + leftContri )
            elif leftContri <= 0 and rightContri > 0:
                self.maxPath = max(self.maxPath, root.val + rightContri)
            else:
                self.maxPath = max(self.maxPath, root.val)

            return max(0, root.val + max(leftContri, rightContri))

        dfs(root)
        return self.maxPath