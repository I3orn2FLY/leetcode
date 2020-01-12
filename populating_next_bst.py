"""
# Definition for a Node.
# class Node:
#     def __init__(self, val, left, right, next):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next
"""


def connect(root: 'Node') -> 'Node':

    parent_leftmost = root

    cur_leftmost = root.left
    while (cur_leftmost):
        last = cur_leftmost
        within = True
        parent = parent_leftmost
        while (parent):
            if within:
                last.next = parent.right
                last = parent.right
            else:
                parent = parent.next
                if parent:
                    last.next = parent.left
                    last = last.next

            within = not within

        prev_leftmost = cur_leftmost
        cur_leftmost = cur_leftmost.left

    return root




