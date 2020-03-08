"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        toReturn = []
        if not root:
            return toReturn
        
        if not root.children:
            toReturn.append(root.val)
            return toReturn
        
        for i in range(len(root.children)):
            toReturn += self.postorder(root.children[i])
            
        toReturn.append(root.val)
        return toReturn