class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = None
        current = None
        hp = list()
        while True:
            size = len(hp) 
            for i in range(len(lists)):
                if lists[i] is None:
                    continue
                else:
                    hp.append(lists[i].val)
                    lists[i] = lists[i].next
            if len(hp) == size:
                break
        heapq.heapify(hp)
        while len(hp) > 0:
            val = heapq.heappop(hp)
            node = ListNode(val)
            if head is None:
                head = node 
                current = node 
            else:
                current.next = node 
                current = node
        return head
    def createIndexDict(self, lists: List[ListNode]) -> dict:
        d = dict()
        i = 0
        for lst in lists:
            d[i] = 0
            i = i+1
        return d
    def getMinIndex(self, lists: List[ListNode], d: dict):
        index = -1
        val = -100000
        for lst in lists:
            d[i] = 0
            i = i+1
