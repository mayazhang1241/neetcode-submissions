class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # Sort by ascending order of start number
        # They overlap if the start of second val is <= end of first val

        # After sorting, iterate through and keep track of previous
        # interval's end

        intervals.sort()
        res = 0;
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)

        return res

            