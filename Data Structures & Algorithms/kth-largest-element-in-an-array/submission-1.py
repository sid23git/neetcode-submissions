class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = nums                    # Line 1: assign nums to heap
        heapq.heapify(heap)            # Line 2: convert into valid Min Heap
        while len(heap) > k:           # Line 3: shrink heap to size k
            heapq.heappop(heap)

        return heapq.heappop(heap) 
