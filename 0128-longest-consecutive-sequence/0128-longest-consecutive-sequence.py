class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        nums=list(set(nums))
        nums.sort()
        res = 0
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                curr += 1
            else:
                res = max(curr, res)
                curr = 1

        return max(curr, res)