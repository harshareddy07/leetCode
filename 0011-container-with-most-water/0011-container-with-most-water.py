class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_num = 0
        while l < r:
            max_num = max(max_num,(r - l) * min( height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            

        return max_num
