from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        end = head
        ch_node = head.next
        while end and ch_node:
            if ch_node.val >= end.val:
                end, ch_node = ch_node, ch_node.next
            elif ch_node.val < head.val:
                head, ch_node.next, end.next, ch_node = ch_node, head, ch_node.next, ch_node.next
            else:
                node = head
                while node.next and node.next.val < ch_node.val:
                    node = node.next

                ch_node.next, node.next, end.next, ch_node = node.next, ch_node, ch_node.next, ch_node.next



        return head


def getLL(values):
    head = ListNode(values[0])
    node = head
    for i in range(1, len(values)):
        node.next = ListNode(values[i])
        node = node.next

    return head

s = Solution()

# s.insertionSortList(getLL([4,2,1,3]))
s.insertionSortList(getLL([-1,3,4,0,5]))


