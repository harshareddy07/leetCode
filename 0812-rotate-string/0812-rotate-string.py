class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        

        if len(s) != len(goal):
            return False
        
        else:
            ss1 = s+s
            if goal in ss1:
                return True
            else:
                return False