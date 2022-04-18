'''https://leetcode.com/problems/kth-smallest-element-in-a-bst/'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        self.nodes.append(root.val)
        self.inorder(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nodes = []
        self.inorder(root)
        self.nodes.sort(reverse=False)
        return self.nodes[k-1]