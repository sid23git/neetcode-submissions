# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        results = []

        queue = deque([root])

        while queue: # I had Some Confusion with the While loop hopefully it Can get Solved 
            size = len(queue)
            empty_list =  []

            for _ in range(size):
                current_node = queue.popleft()
                empty_list.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            results.append(empty_list)

        return results
                


        