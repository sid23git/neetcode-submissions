class Solution:
    def search(self, nums: List[int], target: int) -> int:
       

        l = 0                    # ← Fix here!
        r = len(nums) - 1        # ← Fix here!

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1