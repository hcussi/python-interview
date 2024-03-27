class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f' TreeNode value = {self.val} \n LeftNode = {self.left} \n RightNode = {self.right}'
