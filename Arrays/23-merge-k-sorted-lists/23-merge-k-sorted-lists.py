import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode(0)
        heap = []
        
        for ind, el in enumerate(lists):
            if el:
                heapq.heappush(heap, (el.val, ind))
        
        while heap:
            val, ind = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            
            if lists[ind].next:
                lists[ind] = lists[ind].next
                heapq.heappush(heap, (lists[ind].val, ind))
        return dummy.next
                
        
    
    def mergeKListsBruteForce(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #create a list to append nodes
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l is not None:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next