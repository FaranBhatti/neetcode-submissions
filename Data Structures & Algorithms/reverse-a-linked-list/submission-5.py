# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, temp = None, head

        while head:
            next_node = head.next# store the next node that head points to
            head.next = prev# make head.next to the previous value
            prev = temp# make the prev to temp
            head = next_node# move the head to the next node
            temp = head# update the temp value

        return prev# return prev as that will be the beginning of the last node