class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        remove_idxs = []
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    remove_idxs.append(i)

        j = 0
        k = 0
        res = []
        for i, ch in enumerate(s):
            if j < len(stack) and i == stack[j]:
                j += 1
            elif k < len(remove_idxs) and i == remove_idxs[k]:
                k += 1
            else:
                res.append(ch)


        return "".join(res)