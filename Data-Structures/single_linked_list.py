# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        print_val = self.head
        while print_val is not None:
            print(print_val.val)
            print_val = print_val.next


# start with an empty list
llist = SLinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(4)
# Link the first node with the second node
llist.head.next = second
# Link the second node with the third node
second.next = third

llist.listprint()
print(third.next)   # None = null pointer




