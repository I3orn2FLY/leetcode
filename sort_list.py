# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution:

    def mergeSort(self, head, L):
        if L < 2:
            return head

        left = head
        right = head
        i = -1
        for i in range(L // 2 - 1):
            right = right.next

        l_size = i + 2

        right.next, right = None, right.next

        left = self.mergeSort(left, l_size)
        right = self.mergeSort(right, L - l_size)

        if left.val < right.val:
            head = left
            left = left.next
        else:
            head = right
            right = right.next

        node = head
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next

            node = node.next

        if left:
            node.next = left

        if right:
            node.next = right

        return head

    def sortList(self, head: ListNode) -> ListNode:
        node = head
        L = 0
        while node:
            L += 1
            node = node.next

        if L < 2:
            return head

        return self.mergeSort(head, L)


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
head = build_list([4, 2, 1, 3])
head = s.sortList(head)
printlist(head)