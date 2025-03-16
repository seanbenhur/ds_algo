"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        map_new = {None:None}

        # now we have to clone the nodes
        while curr:
            copy = Node(curr.val)
            map_new[curr] = copy

            curr = curr.next

        curr = head
        while curr:
            copy = map_new[curr]
            copy.next = map_new[curr.next]
            copy.random = map_new[curr.random]

            curr = curr.next
        return map_new[head]
