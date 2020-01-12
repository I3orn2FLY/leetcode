# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree_helper(start_inor, end_inor, preorder_dict, inorder_dict, preorder, inorder):
    if start_inor >= end_inor:
        return None

    root = TreeNode(preorder[buildTree_helper.preor_idx])
    inor_idx = inorder_dict[root.val]
    buildTree_helper.preor_idx += 1
    if start_inor + 1 == end_inor:
        return root

    root.left = buildTree_helper(start_inor, inor_idx, preorder_dict, inorder_dict, preorder, inorder)

    root.right = buildTree_helper(inor_idx + 1, end_inor, preorder_dict, inorder_dict, preorder,
                                  inorder)

    return root


def buildTree(preorder, inorder) -> TreeNode:
    if not inorder:
        return None

    if len(inorder) == 1:
        return TreeNode(inorder[0])

    preorder_dict = {v: i for i, v in enumerate(preorder)}
    inorder_dict = {v: i for i, v in enumerate(inorder)}
    buildTree_helper.preor_idx = 0
    return buildTree_helper(0, len(inorder), preorder_dict, inorder_dict, preorder, inorder)


buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
