class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows) :
            if matrix[i][-1] >= target:
                row = matrix[i]
                l = 0
                r = cols-1  

                while l <= r:
                    m = l + ((r-l)//2)
                    if row[m] == target:
                        return True
                    elif row[m] < target:
                        l = m + 1   
                    else:
                        r = m - 1    

                return  False 

        return False