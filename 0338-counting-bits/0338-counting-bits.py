class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n + 1):
            if i  == offset * 2:
                offset = i
            dp[i] = 1 + dp[i-offset]

        return dp