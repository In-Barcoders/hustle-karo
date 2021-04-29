# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        arr = []
        for i in lists:
            while i != None:
                arr.append(i.val)
                i = i.next
        arr.sort()
        if len(arr) == 0:
            return
        if len(arr) == 1:
            return ListNode(arr[0])
        head = cur = ListNode(arr[0])
        for i in range(1, len(arr)):
            cur.next = ListNode(arr[i])
            cur = cur.next
        return head
