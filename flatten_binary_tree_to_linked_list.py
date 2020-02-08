class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def flat_helper(root):
            if not root:
                return None, None

            h_l, t_l = flat_helper(root.left)
            h_r, t_r = flat_helper(root.right)

            root.left = None

            tail = root

            if h_l:
                root.right = h_l
                t_l.right = h_r
                tail = t_l

            if h_r:
                tail = t_r

            return root, tail

        flat_helper(root)


def build_tree_from_string(inp):
    inp = inp.strip()
    inp = inp[1:-1]
    if not inp:
        return None

    inp_values = [s.strip() for s in inp.split(',')]
    root = TreeNode(int(inp_values[0]))
    queue = [root]
    front = 0
    index = 1
    while index < len(inp_values):
        node = queue[front]
        front = front + 1

        item = inp_values[index]
        index = index + 1
        if item != "null":
            left_n = int(item)
            node.left = TreeNode(left_n)
            queue.append(node.left)

        if index >= len(inp_values):
            break

        item = inp_values[index]
        index = index + 1
        if item != "null":
            right_n = int(item)
            node.right = TreeNode(right_n)
            queue.append(node.right)
    return root


s = Solution()

root = build_tree_from_string("[1,2,null,null,3]")

s.flatten(root)

print()
