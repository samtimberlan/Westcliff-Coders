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
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast and slow pointer. # slow will be mid. keep track of prev
        if not head or not head.next: return None
         # If only two nodes, delete the second one
        if not head.next.next:
            head.next = None
            return head

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next, slow.next = slow.next, None
        return head
        