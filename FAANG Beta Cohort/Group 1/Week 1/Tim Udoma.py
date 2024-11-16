# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # trav. # Save last # Save odd, save even

        if not head or not head.next:
            return head
            
        odd = head
        even_head = even = head.next
        
        while even and even.next:
            # Connect odd to next odd
            odd.next = even.next  
            odd = odd.next
            
            # Connect even to next even
            even.next = odd.next  
            even = even.next
            
        # Connect end of odd list to start of even list    
        odd.next = even_head
        
        return head