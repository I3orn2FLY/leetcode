# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def kthSmallest(root, k):
    if k < 1:
        k = 0

    if root.left:
        n_smaller, l_val = kthSmallest(root.left, k)
    else:
        n_smaller = 0
        l_val = root.val

    if root.right:
        n_bigger, r_val = kthSmallest(root.right, k - 1 - n_smaller)
    else:
        n_bigger = 0
        r_val = root.val

    n = n_smaller + n_bigger + 1

    if k == 0:
        return n, root.val

    if n_smaller == k - 1:
        return n, root.val

    if n_smaller > k - 1:
        return n, l_val

    return n, r_val


def kthSmallest_a(root: TreeNode, k) -> int:
    return kthSmallest(root, k)[1]



root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

print(kthSmallest_a(root, 1))