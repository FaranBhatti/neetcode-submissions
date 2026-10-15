# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# SOLUTION: ITERATIVELY.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        # iterate through linked list starting from the beginning
        while head:
            # store the value before changing the pointer
            nxt = head.next

            # update the head to point to previous
            head.next = prev
            # move prev forward
            prev = head

            # update the head to the value next in the linked list
            head = nxt

        # return the last pointer which is not pointing at the last element in the linkedlist
        return prev