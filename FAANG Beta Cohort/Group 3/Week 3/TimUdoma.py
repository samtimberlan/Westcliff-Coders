# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # trav. Keep count. DFS or BFS
        def dfs(root):
            curr = root
            if not curr: return 0

            return 1 + dfs(curr.left) + dfs(curr.right)
        
        return dfs(root)

        
# Iterative DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        # trav. Keep count. DFS or BFS
        stack = deque([root])
        count = 0

        while stack:
            curr = stack.pop()
            count += 1

            # Only add non-null children
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return count

# BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        # trav. Keep count. DFS or BFS
        q = deque([root])
        count = 0

        while q:
            curr = q.popleft()
            count += 1

            # Only add non-null children
            if curr.right:
                q.append(curr.right)
            if curr.left:
                q.append(curr.left)

        return count

        