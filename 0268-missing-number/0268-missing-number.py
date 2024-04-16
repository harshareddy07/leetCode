class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nm = len(nums)
        for i in range(0,nm+1):
            if i not in nums:
                return i
        