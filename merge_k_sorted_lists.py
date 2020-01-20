import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        heap = []
        for node in lists:
            if node:
                heap.append(node)

        heap = [(node.val, idx, node) for idx, node in enumerate(heap)]
        if not heap:
            return None

        heapq.heapify(heap)
        head = None
        curr = None
        L = len(heap)
        while heap:
            val, _, node = heapq.heappop(heap)
            if not head:
                head = node
                curr = node

            if node.next:
                heapq.heappush(heap, (node.next.val, L, node.next))
                L += 1
            curr.next = node
            curr = node

        return head


inputs = [[1, 4, 5], [1, 3, 4], [2, 6]]


def gen_lists(inputs):
    lists = []
    for inp in inputs:
        head = ListNode(inp[0])
        curr = head
        for i in range(1, len(inp)):
            curr.next = ListNode(inp[i])
            curr = curr.next

        lists.append(head)

    return lists


s = Solution()

s.mergeKLists(gen_lists(inputs))


