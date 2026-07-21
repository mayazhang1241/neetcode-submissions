class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1           # Increment j until it gets to '#'
            
            length = int(s[i:j])
            i = j + 1            # Set i to character after "#"
            j = i + length       # Set j to very last character
            result.append(s[i:j])
            i = j                # Set i to very end of string

        return result
