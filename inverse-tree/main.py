# Problem:
# Given the root of a binary tree, invert the tree, and return its root.
from solution import Solution
from tree_node import TreeNode


if __name__ == '__main__':
    left_node = TreeNode(val = 6)
    right_node = TreeNode(val = 2)
    tree_node = TreeNode(val = 4, left = left_node, right = right_node)

    print(f'Original: \n{tree_node}')
    tree_node = Solution.invert_tree(tree_node)
    print(f'Solution: \n{tree_node}')


