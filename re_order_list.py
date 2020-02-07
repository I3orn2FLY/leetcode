# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


def reverse(head):
    if head is None or head.next is None:
        return head

    rest = reverse(head.next)
    head.next.next = head
    head.next = None

    return rest


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        last = None
        while slow:
            last, slow.next, slow, = slow, last, slow.next

        while last.next:
            head.next, head = last, head.next
            last.next, last = head, last.next


def build_list(inp):
    head = ListNode(inp[0])
    curr = head
    for i in range(1, len(inp)):
        curr.next = ListNode(inp[i])
        curr = curr.next

    return head


def printlist(node):
    s = ""
    while node:
        s += str(node.val) + " "
        node = node.next

    print(s)


s = Solution()

head = build_list([1, 2, 3, 4, 5])
s.reorderList(head)

printlist(head)
