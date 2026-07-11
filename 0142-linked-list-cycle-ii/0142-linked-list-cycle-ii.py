from typing import Optional

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                # Step 2: Find cycle start
                pointer = head

                while pointer != slow:
                    pointer = pointer.next
                    slow = slow.next

                return pointer

        return None