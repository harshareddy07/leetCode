class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singlecount = 0
        visit = {}
        for i in nums:
            if i in visit:
                visit[i] = visit[i] + 1 
              
            if i not in visit:
                visit[i] = 1
             

        for j in nums:
            if j in visit and visit[j] == 1:
                singlecount = j

        return singlecount
        

        