# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Slow and fast pointer algorithm
        # Slow moves through one item at a time, fast moves through two at a time
        # If there is a cycle, fast is guaranteed to eventually catch up to slow
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False