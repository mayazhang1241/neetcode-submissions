class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # edge case: if strs only has one item, return it in result
        if len(strs) == 1:
            return [strs]

        anagrams = defaultdict(list)
        for str in strs:
            sorted_str = "".join(sorted(str))
            anagrams[sorted_str].append(str)
        return list(anagrams.values())
