# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #one pass solution
        left = right = head
        for i in range(n):
            right = right.next
        if not right:
            return head.next
        while right.next:
            right, left = right.next, left.next
        left.next = left.next.next
        return head
        
        
        """#two pass solution
        ptr = head
        length = 0
        
        #requird to find the length
        while ptr is not None:
            ptr = ptr.next
            length = length+1
       
        if length==n:
            return head.next
        ptr = head
        for i in range(1, length-n):
            ptr = ptr.next
        #deleeting the node
        ptr.next = ptr.next.next
        return head"""
            
        
        
    