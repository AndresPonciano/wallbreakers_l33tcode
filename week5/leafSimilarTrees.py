# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List:
        toReturn = []
        if not root.left and not root.right:
            toReturn.append(root.val)
            return toReturn
        
        if root.left:
            toReturn += self.findLeaves(root.left)
            
        if root.right:
            toReturn += self.findLeaves(root.right)
        
        return toReturn
    
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        list1 = self.findLeaves(root1)
        
        list2 = self.findLeaves(root2)
        
        if list1 == list2:
            return True
        
        return False