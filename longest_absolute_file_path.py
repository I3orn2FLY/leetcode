class Solution:
    def lengthLongestPath(self, input: str) -> int:

        paths = input.split("\n")

        res = [0]

        def dfs(root_path, child_tabs, s, e):
            next_tabs = child_tabs + "\t"
            while s < e:
                name = paths[s][len(child_tabs):]
                if root_path:
                    path = f"{root_path}/{name}"
                else:
                    path = name
                s += 1
                if "." in name:
                    res[0] = max(len(path), res[0])
                else:
                    i = s
                    while s < e and paths[s].startswith(next_tabs):
                        s += 1
                    dfs(path, next_tabs, i, s)

        dfs("", "", 0, len(paths))

        return res[0]


s = Solution()

print(s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
