class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num-1 not in num_set:  # Fix 1 ✅
                length = 1
                while (num+length) in num_set:  # Fix 2 ✅
                    length += 1
                longest = max(longest, length)

        return longest


                                                


        