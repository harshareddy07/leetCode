class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        curr_sum = 0
        count = defaultdict(int)
        res = 0

        for r in range(len(nums)):
            count[nums[r]] += 1
            curr_sum += nums[r]

            if r- l + 1 > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    count.pop(nums[l])
                curr_sum -= nums[l]
                l+= 1

            if len(count) == r - l + 1 ==k:
                res = max(curr_sum, res)

        return res