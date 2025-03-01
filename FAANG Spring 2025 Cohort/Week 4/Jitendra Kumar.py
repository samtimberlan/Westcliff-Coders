#Invert Binary Tree : https://leetcode.com/problems/invert-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive: Best For Short trees (depth not too large)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# Time Complexity : O(n) because each node is visited once.
# Space Complexity : The depth of recursion is tree height h, which is O(n) in the worst case (skewed tree) and O(logn) in a balanced tree.

#Iterative: Best For Wide trees (many nodes per level)
from collections import deque
class Solution:
    def invertTree(root: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left  # Swap children
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

# Time Complexity : O(n) because each node is visited once.
# Space Complexity : BFS queue stores nodes at each level, worst case is O(n) (full binary tree with many nodes in the last level).

# Helper function to print tree level-wise (BFS)
def printTree(root):
    if not root:
        print("Tree is empty.")
        return
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing None values for clean output
    while result and result[-1] is None:
        result.pop()
    print("Tree:", result)

# Helper function to build a binary tree from a list (for testing)
def buildTree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# Sample Binary Tree: [4, 2, 7, 1, 3, 6, 9]
#     4
#    / \
#   2   7
#  / \  / \
# 1   3 6  9

tree_values = [4, 2, 7, 1, 3, 6, 9]

# Build Tree
root = buildTree(tree_values)
print("Original:")
printTree(root)

# Test Recursive Approach
print("\nRecursive Inversion:")
inverted_root_recursive = invertTree(root)  # Using the recursive function
printTree(inverted_root_recursive)

# Rebuild tree for iterative test
root = buildTree(tree_values)

# Test Iterative Approach
print("\nIterative Inversion:")
inverted_root_iterative = invertTree(root)  # Using the iterative function
printTree(inverted_root_iterative)


#109. Convert Sorted List to Binary Search Tree: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive approach
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Base case: if the list is empty, return None
        if not head:
            return None
        # If there is only one element, it becomes the tree node.
        if not head.next:
            return TreeNode(head.val)
        # Use two pointers to find the middle element of the list.
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # Disconnect the left half from the middle.
        if prev:
            prev.next = None
        # The middle element becomes the root.
        root = TreeNode(slow.val)
        # Recursively build the left subtree using the left part of the list.
        root.left = self.sortedListToBST(head)
        # Recursively build the right subtree using the right part of the list.
        root.right = self.sortedListToBST(slow.next)
        return root

# Time Complexity : O(n) because each element is pushed and popped at most once, resulting in a total time complexity of O(n).
# Space Complexity : O(n) since the auxiliary stack holds at most O(n) elements, with no extra data structures apart from integer counters.

#Iterative Approach
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        # Convert Linked List to Array
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        # Iterative construction of BST using BFS
        queue = deque()
        root = TreeNode(0)  # Temporary root
        queue.append((root, 0, len(nodes) - 1))  # (TreeNode, left_index, right_index)
        while queue:
            node, left, right = queue.popleft()
            mid = (left + right) // 2
            node.val = nodes[mid]
            # If left subtree exists, create a left child and enqueue it
            if left <= mid - 1:
                node.left = TreeNode(0)
                queue.append((node.left, left, mid - 1))
            # If right subtree exists, create a right child and enqueue it
            if mid + 1 <= right:
                node.right = TreeNode(0)
                queue.append((node.right, mid + 1, right))
        return root


# Helper: Build a linked list from a Python list.
def buildLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper: Print the BST in level-order to verify its structure.
def printTree(root):
    if not root:
        print("Tree is empty.")
        return
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing Nones
    while result and result[-1] is None:
        result.pop()
    print("BST (Level Order):", result)

# Build a sorted linked list (for example: [-10, -3, 0, 5, 9])
values = [-10, -3, 0, 5, 9]
head = buildLinkedList(values)

# Convert the sorted linked list to a height-balanced BST.
bst_root = sortedListToBST(head)

# Print the BST in level-order.
printTree(bst_root)

# Test Case 1: Sorted List to BST
sorted_list = createLinkedList([-10, -3, 0, 5, 9])
bst_root = sortedListToBST(sorted_list)
printBST(bst_root)

# Test Case 2: Empty List
sorted_list = createLinkedList([])
bst_root = sortedListToBST(sorted_list)
printBST(bst_root)

# Test Case 3: Single Node List
sorted_list = createLinkedList([1])
bst_root = sortedListToBST(sorted_list)
printBST(bst_root)

# Test Case 4: Even Number of Nodes
sorted_list = createLinkedList([-10, -3, 0, 5])
bst_root = sortedListToBST(sorted_list)
printBST(bst_root)

#Expected Output
BST: [0, -3, 9, -10, None, 5]
BST: []
BST: [1]
BST: [0, -3, 5, -10]
