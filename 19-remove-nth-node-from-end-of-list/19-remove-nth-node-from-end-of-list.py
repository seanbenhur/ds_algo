# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #two pass solution
        ptr,length=head,0
        while ptr is not None:
            ptr = ptr.next
            length = length+1
        
        if length==n:
            return head.next
        
        ptr = head
        for i in range(1,length-n):
            ptr = ptr.next
        ptr.next = ptr.next.next
        
        return head
            