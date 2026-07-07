class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)          # convert list into a heap
        
        while len(self.heap) > k:          # shrink heap to size k
            heapq.heappop(self.heap)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)     # add new value
        
        if len(self.heap) > self.k:        # if size exceeds k
            heapq.heappop(self.heap)       # remove smallest
        
        return self.heap[0] 
        
