class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L =  0 # INITALIIZINNG OUR POINTERS.
        R = len(heights) -1 

        max_water = 0 

        while L<R :
            water = (R-L) * (min(heights[L], heights[R]))

            max_water = max(max_water, water) # We are upadating the max water term. 


            if heights[L] < heights[R]:
                L += 1
            else : 
                R -= 1 

        return (max_water)
        