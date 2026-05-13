# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            # store next_node
            next_node = head.next

            # reverse the pointer
            head.next = prev

            # push head and prev forward
            prev = head
            head = next_node
        
        return prev