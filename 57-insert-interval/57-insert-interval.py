class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = -1
        
        for i, (x,y) in enumerate(intervals):
            
            if y < newInterval[0]:
                result.append([x,y])
                
            elif newInterval[1] < x:
                i -= 1
                break
                
            else:
                newInterval[0] = min(newInterval[0], x)
                newInterval[1] = max(newInterval[1], y)
                
        return result + [newInterval] + intervals[i+1:]