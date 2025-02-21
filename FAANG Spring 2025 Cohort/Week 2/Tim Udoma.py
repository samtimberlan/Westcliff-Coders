# 1.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solutions: Use a hash table or do it in-place with two pointers
        # Step 1. Go foward to second node. Point second node to previous. Keep doing till null
        if not head or not head.next: return head

        prev = None
        curr = head

        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        return prev
    
    #2. 
    