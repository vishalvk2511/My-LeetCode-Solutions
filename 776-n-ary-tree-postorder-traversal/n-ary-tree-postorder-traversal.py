"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""



class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(root):
            for x in root.children:
                dfs(x)
            res.append(root.val)
        if not root:
            return []
        res = []

        dfs(root)

        return(res)


        


        