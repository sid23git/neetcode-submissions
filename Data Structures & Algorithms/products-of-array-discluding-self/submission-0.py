class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)


        prefix = [1]*n   # This is the way of telling Python that we want a list of 4 1's. 
        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]

        sufix = [1]*n
        for i in range(n-2, -1, -1 ): # (Start, Stop, Step). 
            sufix[i] = sufix [i+1]* nums [i+1]

        output = [prefix[i]* sufix[i] for i in range(n)]
        return output 

        
         
        
        