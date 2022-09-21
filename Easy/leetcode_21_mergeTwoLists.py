# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # declare a dummy node to act as the head of the list
        cur = ListNode()
        list3 = cur

        # while both lists are non-empty
        while list1 and list2:
            # compare the current value of list1 against list2
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        #  if list2 is empty
        if list1:
            cur.next = list1
        #  elif list1 is empty
        elif list2:
            cur.next = list2

        return list3.next


sol = Solution()

