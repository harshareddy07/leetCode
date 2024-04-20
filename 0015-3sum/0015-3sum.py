class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
     
        result= []
        for idx, a in enumerate(nums):
            l = idx +1
            r = len(nums) - 1

            if idx > 0 and nums[idx-1] == a:
                continue
            
            while l < r:
               

                total = a + nums[l] + nums[r]
                if total == 0:
                    result.append([a,nums[l], nums[r]])
                    l += 1
                    while nums[l-1] == nums[l] and l < r :
                        l += 1
                elif total < 0 :
                    l += 1
                else:
                    r -= 1

        return result   