'''https://leetcode.com/problems/middle-of-the-linked-list/'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        count = 0
        node = head
        while node != None:
            count += 1
            node = node.next
        k = count //2
        count = 0
        node = head
        while count <= k:
            if count < k:
                node = node.next
            count += 1
        return node
        
        