REF = 1


class Node:

    def __init__(self, val, neighbors):
        global REF
        self.val = val
        self.neighbors = neighbors
        self.ref = REF
        REF += 1

    def __repr__(self):
        # return str(self.ref)
        return '(' + str(self.ref) + "_" + str(self.val) + ')'
        # return str(self.val)


# def cloneGraph(node: 'Node') -> 'Node':
#     #BFS
#     if not node:
#         return None
#
#     queue = [node]
#     v_to_c = {node: Node(node.val, [])}
#     while queue:
#         vertex = queue.pop(0)
#         clone = v_to_c[vertex]
#         for v in vertex.neighbors:
#             c = v_to_c.get(v)
#             if c is None:
#                 c = Node(v.val, [])
#                 v_to_c[v] = c
#                 queue.append(v)
#
#             clone.neighbors.append(c)
#
#     return v_to_c[node]


#


def cloneGraph(node: 'Node') -> 'Node':
    if not node:
        return None
    # DFS
    stack = [node]
    v_to_c = {node: Node(node.val, [])}
    while stack:
        vertex = stack[-1]
        clone = v_to_c[vertex]
        rm = True
        for v in vertex.neighbors:
            c = v_to_c.get(v)
            if c is None:
                stack.append(v)
                c = Node(v.val, [])
                rm = False
                v_to_c[v] = c
                break

        if rm:
            clone.neighbors += [v_to_c[v] for v in vertex.neighbors]
            stack.pop()

    return v_to_c[node]


node_1 = Node(10, [])
node_2 = Node(20, [])
node_3 = Node(30, [])
node_4 = Node(40, [])

node_1.neighbors.append(node_2)
node_1.neighbors.append(node_4)

node_2.neighbors.append(node_1)
node_2.neighbors.append(node_3)

node_3.neighbors.append(node_2)
node_3.neighbors.append(node_4)

node_4.neighbors.append(node_1)
node_4.neighbors.append(node_3)

clone = cloneGraph(node_1)

print(clone, node_1)
b = '{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}'
a = '{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":1}],"val":2}],"val":1},{"$ref":"4"}],"val":1}'

print(a == b)
