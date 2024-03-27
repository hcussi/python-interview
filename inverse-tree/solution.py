from typing import Optional

from tree_node import TreeNode


class Solution:

    @staticmethod
    def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:

        Solution.invert(root)

        return root

    @staticmethod
    def invert(root: Optional[TreeNode]):
        if root is None:
            return

        left = root.left
        right = root.right

        root.right = left
        Solution.invert(root.right)

        root.left = right
        Solution.invert(root.left)