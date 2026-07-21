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
        
        # Iterate through original list, add values to hashmap
        # To assign random values, can easily grab copy of value stored in
        # hashmap to assign random value

        oldToCopy = { None : None }

        # First pass: cloning nodes and adding to hashmap
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy     # Mapping old node to copy node in hashmap
            curr = curr.next

        # Second pass: set pointers 
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]



