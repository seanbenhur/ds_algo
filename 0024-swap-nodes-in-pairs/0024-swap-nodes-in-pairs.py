# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy

        while head and head.next:
            # store the first pointer
            first = head
            second = head.next


            prev.next = second
            first.next = second.next
            second.next = first

            prev = head
            head = first.next
        return dummy.next

