# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        curr = root
        last_visit = None

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left

            else:
                peek = stack[-1]

                if peek.right and last_visit != peek.right:
                    curr = peek.right

                else:
                    result.append(peek.val)
                    last_visit = stack.pop()

        return result