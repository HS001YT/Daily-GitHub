# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # base case
        if root is None:
            return 0
        
        # This question can be solved by getting the max height between left and right and adding one for that element
        # Time Complexity - O(n) as it iterates through each element
        # Space Complexity - O(height) as recursive functions runs only the height amount of times

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)
