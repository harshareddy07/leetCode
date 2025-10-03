class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited  = {}
        for index, item in enumerate(nums):
            rem = target - item
            if rem in visited :
                return [visited.get(rem), index]
            visited[item] = index