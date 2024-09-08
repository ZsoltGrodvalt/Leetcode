# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
def addition(n1, n2, remainder_prev):
    sum = n1+n2+remainder_prev
    value = sum % 10
    remainder = sum // 10
    # print(f'v:{value}, r:{remainder}')
    return value, remainder

def rest(l_cur, remainder, sum_cur):
    while l_cur.next != None:
        # print(f'sum_head = {sum_head.val}')
        l_cur = l_cur.next
        sum_new = ListNode()
        sum_cur.next = sum_new
        sum_cur = sum_new
        sum_cur.val, remainder = addition(l_cur.val, 0, remainder)
    if remainder != 0:
        sum_new = ListNode()
        sum_cur.next = sum_new
        sum_cur = sum_new
        sum_cur.val = remainder


def addTwoNumbers(l1, l2):
    sum_head = ListNode()
    sum_cur = sum_head
    l1_cur = l1
    l2_cur = l2
    remainder = 0
    # print(head.val)
    while (l1_cur.next != None) & (l2_cur.next != None):
        sum_cur.val, remainder = addition(l1_cur.val, l2_cur.val, remainder)
        # print(f'sum_head = {sum_head.val}')
        l1_cur = l1_cur.next
        l2_cur = l2_cur.next
        sum_new = ListNode()
        sum_cur.next = sum_new
        sum_cur = sum_new

    # exited, but we have to add the last two numbers
    sum_cur.val, remainder = addition(l1_cur.val, l2_cur.val, remainder)

    # both have ended
    if (l1_cur.next == None) & (l2_cur.next == None):
        if remainder != 0:
            sum_new = ListNode()
            sum_cur.next = sum_new
            sum_cur = sum_new
            sum_cur.val = remainder

    # l1 has ended
    if (l1_cur.next == None) & (l2_cur.next != None):
        rest(l2_cur, remainder, sum_cur)

    # l2 has ended
    if (l1_cur.next != None) & (l2_cur.next == None):
        rest(l1_cur, remainder, sum_cur)
    
    return sum_head



#####################################################
# Test case:
# l24 = ListNode(6)
l23 = ListNode(4)
l22 = ListNode(6,l23)
l21 = ListNode(5,l22)
l13 = ListNode(3)
l12 = ListNode(4,l13)
l11 = ListNode(2,l12)

def printList(head):
    node = ListNode()
    node = head
    print(f'[', end='')
    while node.next != None:
        print(f'{node.val},',end='')
        node = node.next
    print(f'{node.val}]')

answer = addTwoNumbers(l11,l21)
printList(l11)
printList(l21)
printList(answer)
#####################################################