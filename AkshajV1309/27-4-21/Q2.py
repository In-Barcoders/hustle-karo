class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None and l2==None :
            return None
        elif l1==None:
            return l2
        elif l2==None:
            return l1
        elif l1.val<=l2.val:
            return ListNode(val=l1.val,next=self.mergeTwoLists(l1.next,l2))
        else:
            return ListNode(val=l2.val,next=self.mergeTwoLists(l1,l2.next))
