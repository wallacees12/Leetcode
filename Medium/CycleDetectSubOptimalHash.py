class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Hash-set - suboptimal, uses o(n) space

        seen = set()
        curr = head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False