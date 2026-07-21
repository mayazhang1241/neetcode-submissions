# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Fast and slow pointer algorithm
        # Fast pointer increments by 2, slow pointer increments by 1
        # This works because if the fast pointer catches back up to
        # the slow pointer, then this indicates there is a cycle
        # If fast pointer is null, then there is no cycle

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False