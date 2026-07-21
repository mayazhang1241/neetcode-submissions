# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Edge case: only one item in list -> remove head

        # === First approach ===
        # Find length k by traversing through list once
        # Index to remove is at k - n

        # === Second approach ===
        # Use fast and slow pointer
        # Slow begins at head, fast begins at n
        # When fast reaches null, slow is at the node right before the one 
        # needed to be removed

        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
