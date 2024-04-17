class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        data = nums
        visit = {}

        for i in data:
            if i in visit and visit[i] == "visited":
                return True
            visit[i] = "visited"
        
        return False
        

            
                