# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # #Brute force

        # curr = head
        # nodes = []

        
        # # Get all nodes in a list
        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next

        # i,j = 0, len(nodes) - 1
        
        # #Iterate until we reach the mid
        # while i < j:
        #     nodes[i].next = nodes[j]
        #     i += 1
        #     if i >= j:
        #         break
        #     # Already incremented i so makes sense!
        #     nodes[j].next = nodes[i]

        #     j -= 1
        # nodes[i].next = None

        # Reverse and Merge

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        # Slow will be halfway through the list
        # Reverse the second half of the list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head,prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
         

        
        