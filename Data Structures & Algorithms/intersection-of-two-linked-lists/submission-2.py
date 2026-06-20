class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeSet = set()
        cur = headA

        while cur :
            nodeSet.add(cur)
            cur  = cur.next 
        
        cur = headB

        while cur:
            if cur in nodeSet:
                return cur
            cur = cur.next 
            
            
        return None