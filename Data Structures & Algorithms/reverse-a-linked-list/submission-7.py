# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            # store next_node in a value
            next_node = head.next

            # reverse the pointer
            head.next = prev

            # move prev and curr forward
            prev = head
            head = next_node

        return prev