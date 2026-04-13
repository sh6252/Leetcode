# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_path(self, res, one_res, node, targetSum):
        one_res.append(node.val)
        if node.left is None and node.right is None:
            if  targetSum - node.val == 0:
                res.append(one_res.copy())
            one_res.pop()
            return
        if node.left is not None:
            self.find_path(res, one_res, node.left, targetSum - node.val)
        if node.right is not None:
            self.find_path(res, one_res, node.right, targetSum - node.val)
        one_res.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        result = []
        path = []
        self.find_path(result, path, root, targetSum)
        return result
        