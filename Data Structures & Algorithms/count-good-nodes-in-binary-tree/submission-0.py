# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if node is None:                          # Base case: no node, no good nodes
                return 0
            
            count = 1 if node.val >= max_so_far else 0   # Is current node good?
            max_so_far = max(max_so_far, node.val)        # Update max for children
            
            left_count = dfs(node.left, max_so_far)       # Count good nodes on left
            right_count = dfs(node.right, max_so_far)     # Count good nodes on right
            
            return count + left_count + right_count        # Combine all counts
        
        return dfs(root, root.val)
            