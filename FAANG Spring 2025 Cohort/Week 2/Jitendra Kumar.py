#Reverse Linked List : https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
# Time Complexity : O(n) because we go through all the nodes once.
# Space Complexity : O(1) because we only use a few extra variables.

#Delete the Middle Node of a Linked List : https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
# Time Complexity : O(n) because we go through the list once.
# Space Complexity : O(1) since we only use a few extra variables, no extra memory for data storage.
