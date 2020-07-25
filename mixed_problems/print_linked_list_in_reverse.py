class ListNode:
    def __init__(self,val,nextpt):
        self.val = val
        self.next = nextpt

def reverse_py(l1):
    if l1 == None:
        return
    reverse_py(l1.next)
    print(l1.val)

def main(l1head):
    if l1head == None:
        return
    else:
        reverse_py(l1head)