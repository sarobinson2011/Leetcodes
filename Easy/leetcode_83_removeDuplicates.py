""" draft solution to leetcode_83_deleteDuplicates  """

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        temp = head
        while temp is not None and temp.next is not None:
            while temp.val == temp.next.val:
                temp.next = temp.next.next
                if temp.next is None:
                    break
            temp = temp.next
        return head


sol = Solution()

# First build the linked list
n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(2)
n5 = ListNode(3)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Pass the linked list as an argument to the function
sol.deleteDuplicates(n1)
