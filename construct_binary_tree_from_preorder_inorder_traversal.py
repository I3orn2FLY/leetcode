class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def build_tree(inorder, preorder, ino2pre, start_ino, end_ino):
    if end_ino - start_ino <= 0:
        return None
    min_pre_idx = len(preorder)
    for idx in range(start_ino, end_ino):
        min_pre_idx = min(min_pre_idx, ino2pre[idx])

    node = TreeNode(preorder[min_pre_idx])
    for idx in range(start_ino, end_ino):
        if inorder[idx] == preorder[min_pre_idx]:
            ino_idx = idx
            break

    node.left = build_tree(inorder, preorder, ino2pre, start_ino, ino_idx)
    node.right = build_tree(inorder, preorder, ino2pre, ino_idx + 1, end_ino)

    return node


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(None)
        stack = [(root, 0, len(inorder))]

        ino_dict = {val: idx for idx, val in enumerate(inorder)}
        preo_idx = 0
        while stack:
            node, start_ino, end_ino = stack.pop()
            node.val = preorder[preo_idx]
            ino_idx = ino_dict[node.val]
            preo_idx += 1

            if start_ino < ino_idx:
                node.left = TreeNode(None)

            if ino_idx < end_ino - 1:
                node.right = TreeNode(None)

            if node.right:
                stack.append((node.right, ino_idx + 1, end_ino))

            if node.left:
                stack.append((node.left, start_ino, ino_idx))

        return root


s = Solution()

root = s.buildTree([3, 1, 2, 4], [1, 2, 3, 4])

print()
