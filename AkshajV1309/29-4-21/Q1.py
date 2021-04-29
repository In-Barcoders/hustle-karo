class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0,head)
        groupPrev = dummy
        while True:
            kth = self.getk(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next
            prev,curr = kth.next,groupPrev.next
            while curr != groupNext:
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next
    def getk(self,curr,k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
