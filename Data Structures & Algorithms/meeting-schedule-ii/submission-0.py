"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # Create 2 arrays of start and end times
        # Sort both arrays


        startTimes = sorted([i.start for i in intervals])
        endTimes = sorted([i.end for i in intervals])

        # res is max # of days of count variable (output)
        res, count = 0, 0

        # s = position in startTimes array, e = position in endTimes array
        s, e = 0, 0

        while s < len(intervals):
            if startTimes[s] < endTimes[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            res = max(res, count)

        return res