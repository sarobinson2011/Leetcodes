# Definition for singly-linked list.
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head_val = None

    def print_lists(self):
        out = []
        print_val = self.head_val
        while print_val is not None:
            out.append(print_val.val)
            print_val = print_val.next
        # for i in range(1):
        print(f'list =',out)

    def merge_two_lists(self, list1: [Node], list2: [Node]) -> [Node]:
        """ first declare a dummy node to act as the head of the list """
        cur = Node()
        merged_list = cur

        # while both lists are non-empty
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

        if list2:       # if list1 is empty
            cur.next = list2
        elif list1:     # elif list 2 is empty
            cur.next = list1

        # print(merged_list.next)
        return merged_list.next


# create 3 instances of linked lists
my_list1 = Linkedlist()
my_list2 = Linkedlist()
output_list = Linkedlist()
# set the 'Node' values in list1 and list2
my_list1.head_val = Node('1')
my_list2.head_val = Node('1')
list1_2 = Node('3')
list2_2 = Node('5')
list1_3 = Node('4')
list2_3 = Node('6')
# connect 1st node to 2nd node
my_list1.head_val.next = list1_2
my_list2.head_val.next = list2_2
# connect 2nd node to 3rd node
list1_2.next = list1_3
list2_2.next = list2_3

# run the print_lists function on the 2 lists
my_list1.print_lists()
my_list2.print_lists()

output_list.merge_two_lists(my_list1.head_val, my_list2.head_val)
output_list.print_lists()














