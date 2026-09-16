class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []

        # use a hashmap to store the sublists
        # frequency map : sublist

        anagrams = defaultdict(list)

        if len(strs) == 1:
            return [strs]

        for s in strs:
            sorted_s = "".join(sorted(s))
            anagrams[sorted_s].append(s)

        return list(anagrams.values())



