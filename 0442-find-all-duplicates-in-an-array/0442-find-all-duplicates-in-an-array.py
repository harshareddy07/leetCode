class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        visited = set()
        final = []
        for i in nums:
           # visit[i] = visit.get(i,0) + 1
            if i in visited:
                final.append(i)
            
            visited.add(i)
        return final 


        