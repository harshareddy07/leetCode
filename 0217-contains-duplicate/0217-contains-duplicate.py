class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for index, num in enumerate(nums):
            if num in visited:
                return True
            visited[num] = index

        return False
        