class Solution:
    def is_valid(self, node, min_val, max_val):
        if node is None:
            return True

        return (
            min_val < node.val < max_val
            and self.is_valid(node.left, min_val, node.val)
            and self.is_valid(node.right, node.val, max_val)
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid(root, float("-inf"), float("inf"))