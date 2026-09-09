"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #for i in node.neighbors:
        #   print(i.val)
        visit = {}
        def dfs(node):
            if not node:
                return None
            if node in visit:
                return visit[node]

            nodeC = Node(node.val,[])
            visit[node] = nodeC
            for n in node.neighbors:
                tempNode = dfs(n)
                nodeC.neighbors.append(tempNode)

            return nodeC

        return dfs(node)
