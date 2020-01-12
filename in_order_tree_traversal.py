class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def inorderTraversal(root: TreeNode):
    if not root:
        return []

    visited = set()
    stack = [root]
    ans = []
    while len(stack) > 0:
        node = stack[-1]

        visited.add(node)

        if node.left and node.left not in visited:
            stack.append(node.left)

        else:
            ans.append(stack.pop().val)

            if node.right and node.right not in visited:
                stack.append(node.right)


root = TreeNode(1)

root.right = TreeNode(2)
root.right.left = TreeNode(3)


inorderTraversal(root)
