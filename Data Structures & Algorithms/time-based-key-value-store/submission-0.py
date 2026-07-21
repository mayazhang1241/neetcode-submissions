class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Get list of [value, timestamp] pairs for each key
        result, values = "", self.timeMap.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            # If timestamp at index m is <= timestamp
            if values[m][1] <= timestamp:
                # Update result bc we found best value so far
                result = values[m][0]
                # Keep looking for a more "recent" one that is also
                # <= timestamp
                l = m + 1
            else: 
                r = m - 1

        return result