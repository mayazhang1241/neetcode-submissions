class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Unsorted, so must sort list first
        # Sort based on start values, end values don't rlly matter
        # O(n)

        # If curr.end >= prev.beginning and curr.start <= prev.end, merge
        # O(logn)

        # i = interval
        intervals.sort(key = lambda i : i[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1] # prev interval end

            # If start <= last end, it's overlapping
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)   # Find new end

            # Non-overlapping
            else:
                output.append([start, end])

        return output

