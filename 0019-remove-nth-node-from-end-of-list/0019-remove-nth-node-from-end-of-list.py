from typing import Optional

class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Create a gap of n + 1 nodes
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # Delete nth node from end
        slow.next = slow.next.next

        return dummy.next