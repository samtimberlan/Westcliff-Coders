from typing import Optional

#Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = val

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the start of the merged list
        dummy = ListNode(-1)
        current = dummy # Pointer to build the merged list

        # Traverse both lists until one becomes mepty
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1 # Add the smaller node to the merged list
                list1 = list1.next # Move to the next node in list1
            else:
                current.next = list2
                list2 = list2.next
        
        # If any elements remain in either list, attach them
        if list1:
            current.next = list1
        if list2:
            current.next - list2

        # Return the merged list, starting from the first real node (skip the dummy)
        return dummy.next
    
# Time Complexity O(n)
# Space Complexity O(1)
