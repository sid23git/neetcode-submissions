class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # I will use hash  map here. then rturn the repeated int. 

        hash_map = {}

        for i in nums:


            if i in hash_map:
                return i 

            hash_map[i] = True 
        return -1 

        



        