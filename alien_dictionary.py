def idx(c):
    return ord(c) - ord('a')


def alienOrder(words):
    nodes = set()
    for word in words:
        for c in word:
            nodes.add(c)

    G = {node: set() for node in nodes}

    for i in range(len(words) - 1):
        for j in range(min(len(words[i]), len(words[i + 1]))):
            c1, c2 = words[i][j], words[i + 1][j]
            if c1 != c2:
                G[c2].add(c1)
                break

    visited = [True] * 26

    for node in nodes:
        visited[idx(node)] = False

    stack_seen = [False] * 26

    res = []
    for node in nodes:
        if not visited[idx(node)]:
            stack = [node]
            stack_seen[idx(node)] = True
            visited[idx(node)] = True
            while stack:
                vertex = stack[-1]
                rm = True
                for v in G[vertex]:
                    if stack_seen[idx(v)]:
                        return ""
                    if not visited[idx(v)]:
                        stack.append(v)
                        stack_seen[idx(v)] = True
                        visited[idx(v)] = True
                        rm = False
                        break

                if rm:
                    stack_seen[idx(vertex)] = False
                    res.append(stack.pop())

    return "".join(res)


res = alienOrder([
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
])

print(res)

res = alienOrder(['eff', 'fg'])
print(res)
res = alienOrder(["wrt","wrf","er","ett","rftt","te"])
print(res)

