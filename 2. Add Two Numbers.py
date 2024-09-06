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
    # l1 has ended

    # l2 has ended

    # both have ended


    # exited, but we have to add the last two numbers
    sum_cur.val, remainder = addition(l1_cur.val, l2_cur.val, remainder)
    # only works if the lengths are the same
    answer = []
    sum_cur = sum_head
    while sum_cur.next != None:
        answer.append(sum_cur.val)
        sum_cur = sum_cur.next
    answer.append(sum_cur.val)
    return answer 

n1 = ListNode(4)
n2 = ListNode(6,n1)
l2 = ListNode(5,n2)
n4 = ListNode(3)
n5 = ListNode(4,n4)
l1 = ListNode(2,n5)

print(addTwoNumbers(l1,l2))