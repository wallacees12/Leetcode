# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 or not list2:
            return list1 if list1 else list2

        val = list1.val if list1.val < list2.val else list2.val
        h3 = ListNode(val)
        current = h3

        if list1.val < list2.val:
            list1 = list1.next
        else:
            list2 = list2.next

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list2 if list2 else list1

        return h3

    
            


            
        