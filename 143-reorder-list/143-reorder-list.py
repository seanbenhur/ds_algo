# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #find middle of the list
        if not head:
            return []
        slow,fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        #reverse the second half of the list
        prev,curr = None,slow.next
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        slow.next = None
            
        #merge the two lists
        head1, head2 = head, prev
        while head2 is not None:
            next_node = head1.next
            head1.next = head2
            head1 = head2
            head2 = next_node
            
            
        
        
        