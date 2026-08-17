# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def validPathSum(root, target):
            if not root:
                return False

            target -= root.val
            if not root.left and not root.right and target == 0:
                return True
            
            if validPathSum(root.left, target):
                return True
            
            if validPathSum(root.right, target):
                return True

            target += root.val
            return False

        return validPathSum(root, targetSum)