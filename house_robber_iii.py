class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution:

    def max_rob(self, root):
        if not root:
            return 0, 0
        rob_l, rob_l_ch = self.max_rob(root.left)
        rob_r, rob_r_ch = self.max_rob(root.right)

        res_ch = rob_l + rob_r

        res = max(res_ch, root.val + rob_l_ch + rob_r_ch)

        return res, res_ch

    def rob(self, root: TreeNode) -> int:
        return self.max_rob(root)[0]


s = Solution()
