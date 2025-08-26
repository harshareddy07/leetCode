class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not intervals:
            return []
        
        # Step 1: Sort by start times
        intervals.sort(key=lambda x: x[0])
        
        res = [intervals[0]]  # start with first interval

        for start, end in intervals[1:]:
            prev = res[-1][1]
            
            if start <= prev:
                res[-1][1] = max(prev, end)

            else:
                # No overlap → add new interval
                res.append([start, end])

        return res
        