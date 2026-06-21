class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0) # we haave Create a dummy Node with 0 value 
        dummy.next = head 
        slow = dummy 
        fast = head 

        while n > 0:
            fast = fast.next 
            n -=1 
            

        while fast:  
            slow= slow.next 
            fast = fast.next 

        slow.next = slow.next.next
        return dummy.next