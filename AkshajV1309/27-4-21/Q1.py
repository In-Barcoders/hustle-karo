class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ah=be=head
        for i in range(n):
            ah=ah.next
        if ah==None:
            return head.next
        while ah.next!=None:
            ah=ah.next
            be=be.next
        be.next=be.next.next
        return head
