class Solution(object):
    def twoSum(self, nums, target):
        visit = {}
        for index, n in enumerate(nums):
            rem = target - n 
            if rem in visit:
                return [visit.get(rem), index]
            visit[n] = index
        return
        