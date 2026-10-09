class Solution:

    def encode(self, strs: List[str]) -> str:
        # when merging, put the number of characters of each word right before
        # put a special character in between to separate length from when the word starts
        # ["Hello", "World"] --> "5%Hello5%World"

        res = []
        encoded_str = ""

        for s in strs:
            encoded_str = str(len(s)) + "%" + s
            res.append(encoded_str)

        encoded_str = "".join(res)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # "5%Hello5%World" --> ["Hello", "World"]

        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '%':
                j += 1
            length = int(s[i:j])

            i = j + 1
            j = i + length

            res.append(s[i:j])
            i = j

        return res
