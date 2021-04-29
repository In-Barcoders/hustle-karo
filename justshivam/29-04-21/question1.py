# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head

        def reverse(node, digits):
            cur, res = node, None
            for i in range(digits-1):
                cur = cur.next
                if cur == None:
                    return
                if i == digits-2:
                    res = cur
            cur, store = node, res.next
            for i in range(k):
                x = cur.next
                cur.next = store
                store = cur
                cur = x
            return [res, node]
        res = cur = reverse(head, k)
        while cur[1].next != None:
            new = reverse(cur[1].next, k)
            if new == None:
                break
            cur[1].next = new[0]
            cur = new
        return res[0]
