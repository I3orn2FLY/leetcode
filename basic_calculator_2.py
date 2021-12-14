# this solution is not optimal, optimal is solved by stack principles
# even more optimal is done without stack if current number and result are kept in different variables
class Solution:

    def calculate(self, s: str) -> int:
        signs = []
        nums = []
        num = []
        for i, ch in enumerate(s):
            if ch.isdigit():
                num.append(ch)

            if not ch.isdigit() or (i == len(s) - 1 and ch.isdigit()):
                if num:
                    nums.append(int("".join(num)))
                    num = []
                if ch in {'+', '-', '/', '*'}:
                    signs.append(ch)

        if not signs:
            return nums[0]

        class Node:
            def __init__(self, val):
                self.val = val
                self.sign = None
                self.next = None

        root = Node(nums[0])
        root.sign = signs[0]
        prev_node = root
        for i in range(1, len(nums)):
            node = Node(nums[i])
            if i != len(signs):
                node.sign = signs[i]
            prev_node.next = node
            prev_node = node

        def mult_div(root):
            node = root.next
            while node and root.sign in {"*", "/"}:
                if root.sign == "*":
                    root.val *= node.val
                else:
                    root.val = int(root.val / node.val)
                root.sign = node.sign
                root.next = node.next
                node = node.next

        res = 0
        sign = '+'
        while root:
            mult_div(root)
            if sign == "+":
                res += root.val
            else:
                res -= root.val
            sign = root.sign
            root = root.next

        return res


s = Solution()
print(s.calculate("  3+5 / 2 -7            "))
