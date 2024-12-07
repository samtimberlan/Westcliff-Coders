#Merge Two Binary Trees: https://leetcode.com/problems/merge-two-binary-trees/description/
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 == None:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
    # Time complexity O( total number of nodes in the smaller tree)
    # Space complexity O(height of the tree)

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        stack = [(root1, root2)]
        while stack:
            t1, t2 = stack.pop()
            if t1 is None or t2 is None:
                continue
            t1.val += t2.val
            if t1.left is None:
                t1.left = t2.left
            else:
                stack.append((t1.left, t2.left))
            if t1.right is None:
                t1.right = t2.right
            else:
                stack.append((t1.right, t2.right))
        return root1
    # Time complexity O( total number of nodes in the smaller tree)
    # Space complexity O(height of the tree)
