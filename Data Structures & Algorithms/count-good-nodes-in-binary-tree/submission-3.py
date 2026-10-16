# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, max_node_val):
            if not root:
                return 0
            good = 1 if root.val >= max_node_val else 0

            max_node_val = max(root.val ,  max_node_val)

            left = dfs(root.left, max_node_val)
            right = dfs(root.right, max_node_val)

            return left+ right +good

        return dfs(root, root.val)