'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    temp1 = l1
    temp2 = l2
    temp = carry = 0
    result = None
    temp_node = None
    prev_node = None
    while temp1 != None and temp2 != None:
        sum_val = temp1.val + temp2.val + carry
        carry = sum_val // 10
        sum_val = sum_val % 10
        temp_node = ListNode(sum_val,None)
        if result == None:
            result = temp_node
        else:
            prev_node.next = temp_node
        prev_node = temp_node
        temp1 = temp1.next
        temp2 = temp2.next
    
    if carry== 0:
        if temp1 != None:
            prev_node.next = temp1
    
        if temp2 != None:
            prev_node.next = temp2
    else:
        if temp1!=None:
            temp = temp1
        elif temp2 != None:
            temp = temp2
        else:
            temp_node = ListNode(carry,None)
            prev_node.next = temp_node
            temp = None
        while temp != None:
            sum_val = temp.val + carry
            carry = sum_val // 10
            sum_val = sum_val % 10
            temp_node = ListNode(sum_val,None)
            prev_node.next = temp_node
            prev_node = temp_node
            temp = temp.next
        if carry != 0:
            temp_node = ListNode(carry,None)
            prev_node.next = temp_node
    return result

if __name__ == '__main__':
    #Define l1 and l2 linked lists
    l1 = None
    l2 = None 
    result = addTwoNumbers(l1,l2)