# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or head == None:
            return head
        cur = head
        l = 1
        while cur.next != None:
            cur = cur.next
            l += 1
        r = k % l
        cur.next = head
        p1 = p2 = cur
        for i in range(r):
            p2 = p2.next
        while p2 != cur:
            p2 = p2.next
            p1 = p1.next
        store = p1.next
        p1.next = None
        return store
