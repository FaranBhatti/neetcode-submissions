# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            temp = head             # store head
            next_node = head.next   # storage ref to next node
            head.next = prev        # point the current head node to the previous
            prev = temp             # update previous to the temp because thats where you stored the head
            head = next_node        # update the head to the next node
        return prev