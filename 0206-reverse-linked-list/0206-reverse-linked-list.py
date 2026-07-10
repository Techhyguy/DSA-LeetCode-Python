from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current is not None:
            next_node = current.next   # Save next node
            current.next = prev        # Reverse pointer
            prev = current             # Move prev forward
            current = next_node        # Move current forward

        return prev