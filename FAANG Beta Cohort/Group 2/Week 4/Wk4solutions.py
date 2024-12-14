from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if not node:
                return
            # Traverse left subtree
            inorder(node.left)
            # Visit current node
            result.append(node.val)
            # Traverse right subtree
            inorder(node.right)

        inorder(root)
        return result

# Examples
# Helper function to build a tree from a list
def build_tree(values):
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    children = nodes[::-1]
    root = children.pop()

    for node in nodes:
        if node:
            if children:
                node.left = children.pop()
            if children:
                node.right = children.pop()

    return root

# Example 1
root1 = build_tree([1, None, 2, 3])
solution = Solution()
print(solution.inorderTraversal(root1))  # Output: [1, 3, 2]

# Example 2
root2 = build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
print(solution.inorderTraversal(root2))  # Output: [4, 2, 6, 5, 7, 1, 3, 9, 8]

# Example 3
root3 = build_tree([])
print(solution.inorderTraversal(root3))  # Output: []

# Example 4
root4 = build_tree([1])
print(solution.inorderTraversal(root4))  # Output: [1]
