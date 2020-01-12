class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val) + ":" + str(self.next)


def reverse(head):
    curr_node = head
    prev_node = None

    while (curr_node):
        temp = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = temp

    return prev_node


h = ListNode(10)
h.next = ListNode(20)
h.next.next = ListNode(30)
h.next.next.next = ListNode(40)

def hello(h):
    h = reverse(h)
    reverse(h)

print(h)
hello(h)
print(h)