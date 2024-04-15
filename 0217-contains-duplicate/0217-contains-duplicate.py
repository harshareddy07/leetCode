class Solution(object):
    def containsDuplicate(self, nums):
        seen = {}
     
        for item in nums:
            if item  in seen and seen[item] == "visited":
                return True
            seen[item] = "visited"
          
        
        return False