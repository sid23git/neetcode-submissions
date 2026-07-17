class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = {}

        for i, n in enumerate(nums):
            diffrence = target - n
            if diffrence in result:
                return [result[diffrence], i ]

            result[n] = i 


        





        