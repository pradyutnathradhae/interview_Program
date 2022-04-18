'''https://leetcode.com/problems/increasing-order-search-tree/'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solveleft(self,root):
        if root == None:
            return
        self.solveleft(root.right)
        self.tempnodes.append(root)
        self.solveleft(root.left)
    def solveright(self,root):
        if root == None:
            return
        self.solveright(root.left)
        self.tempnodes.append(root)
        self.solveright(root.right)
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.tempnodes = [root]
        self.solveleft(root.left)
        node = self.tempnodes[-1]
        # self.tempnodes.pop()
        self.tempnodes.reverse()
        self.solveright(root.right)
        for nd in range(len(self.tempnodes)-1):
            self.tempnodes[nd].left = None
            self.tempnodes[nd].right = self.tempnodes[nd+1]
        self.tempnodes[-1].left = None
        self.tempnodes[-1].right = None
        return node