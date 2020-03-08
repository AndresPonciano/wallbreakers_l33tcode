# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorder(self, root: TreeNode) -> List:        
        toReturn = []
        
        toReturn.append(root.val)
        
        if not root.left and not root.right:
            return toReturn
        
        if root.left:
            toReturn += self.preorder(root.left)
            
            if not root.right:
                toReturn.append(None)
            
            
        if root.right:
            if not root.left:
                toReturn.append(None)     
            
            toReturn += self.preorder(root.right)
            
            
        return toReturn
        
        
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        list1 = self.preorder(p)
        list2 = self.preorder(q)
        
        if list1 == list2:
            return True
        
        return False