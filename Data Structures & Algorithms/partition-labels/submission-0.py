class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # Each character in the string has a first and last index it appears in
        # Store last index of each character in hash map
        
        # Iterate through each character in string
        # Treat each index as start of potential substring
        # Track the end of that substring by taking the max of the last 
        # index of all the characters we've seen so far

        lastIndex = {}

        # Creates a map of each character to its last index in the string
        # Does this by overwriting the index each time the character is come
        # across again
        for i, char in enumerate(s):
            lastIndex[char] = i

        result = []  # Stores sizes of substrings
        size = end = 0  # Tracks how big current substring is

        # Go through string and keep incrementing the size of the substring
        # until the end reaches the last furthest occurence of 
        # any character we've seen so far in this substring
        for i, char in enumerate(s):
            size += 1
            end = max(end, lastIndex[char])

            # Resets everything and adds the size to the result
            if i == end:
                result.append(size)
                size = 0

        return result