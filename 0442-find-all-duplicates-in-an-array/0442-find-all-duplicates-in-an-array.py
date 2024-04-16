class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        visit = {}
        final = []
        for i in nums:
            visit[i] = visit.get(i,0) + 1
            if visit[i] > 1:
                final.append(i)
        return final 


        