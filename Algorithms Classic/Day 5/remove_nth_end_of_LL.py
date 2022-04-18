'''https://leetcode.com/problems/remove-nth-node-from-end-of-list/'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        count = 0
        node = head
        while node != None:
            count += 1
            node = node.next
        k = count- n
        if k == 0:
            head = head.next
        else:
            count = 0
            node = head
            while count <= k:
                count += 1
                if count == k:
                    node.next = node.next.next
                    break
                node = node.next
        return head
                