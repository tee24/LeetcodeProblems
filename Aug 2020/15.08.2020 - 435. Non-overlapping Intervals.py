class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        rem = 0
        end = float('-inf')
        intervals = sorted(intervals, key=lambda x:x[1]) # sort by ends O(nlog(n)), we remove the interval with largest endpoint to give more "room" for non overlapping intervals

        for i in intervals:
            if i[0] >= end: # if there is no overlap
                end = i[1]
            else:
                rem+=1 
        return rem
#Space, Time: O(1), O(nlog(n))