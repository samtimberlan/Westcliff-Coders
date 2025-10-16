# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse current node's pointer
            prev = current            # Move prev to current node
            current = next_node       # Move to next node
        return prev
    
# Time Complexity: O(n) because we iterate through the list once.
# Space Complexity: O(1) because we only use a few extra variables, no extra memory for data storage.


    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
                return None
            
        # Initialize a dummy node
        # Initialize a dummy node
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
            
        # Traverse the list with two pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node
        slow.next = slow.next.next
            
            # Return the modified list
        return dummy.next
    
# Time Complexity: O(n) because the algorithm traverses the list once to identify and remove the middle node.
# Space Complexity: O(1) because the algorithm utilizes a constant amount of extra space, primarily for the slow and fast pointers and a dummy node.



