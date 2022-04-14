'''https://leetcode.com/problems/closest-binary-search-tree-value/'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root, val):
        node = root
        if node == None:
            return None
        soln = node.val
        while node != None:
            if abs(node.val - val) < abs(soln - val):
                soln = node.val
            if val > node.val:
                node = node.right
            elif val == node.val:
                break
            else:
                node = node.left
        return soln


