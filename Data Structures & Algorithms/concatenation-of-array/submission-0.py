class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)  # we are given a zero indexed array. 
        ans = []

        for i in range(2):
            for num in nums:
                ans.append(num)


        return ans 