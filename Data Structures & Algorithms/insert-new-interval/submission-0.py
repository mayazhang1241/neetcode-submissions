class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # Visualize each interval as a line
        # Intervals may not overlap ranges

        # Check to see if newInterval.end is < interval.start

        # Check to see if newInterval.start is > interval.end

        # If both of these cases are false, then must mean they overlap
        # If overlapping, merge them
        
        # Merge by taking minimum of both of them and maximum of both
        # of them and create a new merged interval

        res = []

        for i in range(len(intervals)):
            # Not overlapping edge cases
            # Check if newInterval.end is entirely before interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # Check if newInterval.start is entirely after interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # Overlapping
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])]

        res.append(newInterval)

        return res
                