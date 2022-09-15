# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        """ merge lists """
        merged_list = [ListNode]

        merged_list.val = list1.val

        while list2.next != None
            if list1.next > list2.val:
                merged_list.next = list2.val
            else:
                merged_list.next = list1.val











