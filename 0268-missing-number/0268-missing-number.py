class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

       # nm = len(nums)
     
      #  for i in range(0,nm+1):
       #     if i not in nums:
        #        return i

       # n = len(nums)
        #expectedSum = (n*(n+1))//2
        #actualSum = sum(nums)
        #return expectedSum-actualSum

        res = len(nums)

        for i in range(len(nums)):
            res += (i-nums[i])

        return res
        