"""Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input."""




class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x:x[0])
        merged = []
        
        for inter in intervals:
            
            if not merged or merged[-1][-1]<inter[0]:
                merged.append(inter)
                
            else:
                merged[-1][-1] = max(merged[-1][-1],inter[-1])
                
        return merged