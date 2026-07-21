class Solution:

    # We can simply join the list of strings into a string, but then
    # when we go to decode, how will we know which word is which?

    # Question: Can a string just be a number?
    # Answer: Yes

    # Must find a way to denote how long each string is
    # Encode each string like: hello --> 5#hello
    # The # sign is to separate length and string

    def encode(self, strs: List[str]) -> str:
        # list of strings --> single string
        # ["Hello","World"] --> "5#Hello5#World"

        res = []
        encoded_string = ""

        for s in strs:
            encoded_str = str(len(s)) + "#" + s
            res.append(encoded_str)

        encoded_string = "".join(res)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # encoded_string --> list of strings
        # "5#Hello5#World" --> ["Hello","World"]

        # iterate through the string
        # use two pointer: i at the integer, j to hop to the end of the string
        
        decoded = []
        i = 0

        while i < len(s):
            j = i

            # find the length
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            # get the string
            i = j + 1
            j = i + length

            decoded.append(s[i:j])
            i = j

        return decoded











