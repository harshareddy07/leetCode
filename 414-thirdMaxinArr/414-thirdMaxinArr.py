class Solution(object):
    def thirdMax(self, nums):
        max_1 = max_2 = max_3 = float('-inf')
        seen = set()
        for i in range(0, len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])

            if nums[i] >  max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = nums[i]
            elif nums[i] > max_2:
                max_3 = max_2
                max_2 = nums[i]
            elif nums[i] > max_3:
                max_3 = nums[i]
                

        # Return third max if exists, else fall back
        if max_3 != float('-inf'):
            return max_3
        else:
