'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    result = None
    tempnode = prevnode = temp = None
    while l1 != None and l2 != None:
        if l1.val <= l2.val:
            tempnode = l1
            l1 = l1.next
        else:
            tempnode = l2
            l2 = l2.next
        if result == None:
            result = tempnode
            prevnode = tempnode
        else:
            prevnode.next = tempnode
            prevnode = tempnode
    if l1!= None:
        temp = l1
    if l2 != None:
        temp = l2
    if prevnode == None:
        prevnode = result = temp
    else:
        prevnode.next = temp
    return result