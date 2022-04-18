'''https://leetcode.com/problems/convert-bst-to-greater-tree/'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root):
        if root == None:
            return
        self.solve(root.right)
        self.val += root.val
        root.val = self.val
        self.solve(root.left)
        
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.val = 0
        self.solve(root)
        return root