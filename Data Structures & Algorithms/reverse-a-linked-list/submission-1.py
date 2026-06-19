# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next = curr.next      # Save next
            curr.next =  prev # Reverse arrow
            prev = curr      # Move prev
            curr = next      # Move curr

        return prev          # New he

        