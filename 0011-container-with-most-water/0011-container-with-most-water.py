class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l , r = 0 , len(height) - 1
        maxHeight = 0
        while l < r:
            maxHeight = max(maxHeight, min(height[l],height[r]) * (r-l))

            if height[l] < height[r]:
                l +=1
            else:
                r -= 1
        
        return maxHeight
