class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones] # giving a -ve Sign to every elemnet in the heap to Conveert it into max heap 
        heapq.heapify(heap)           # convert to heap

        while len(heap)>1:
            y =  -heapq.heappop(heap)
            x =  -heapq.heappop(heap)

            if x != y:
               heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0 