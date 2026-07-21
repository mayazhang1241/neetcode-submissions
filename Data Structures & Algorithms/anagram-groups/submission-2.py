class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []

        # use a hashmap to store the sublists
        # frequency map : sublist
        
        anagrams = defaultdict(list)

        # edge case: if strs only has one item, return it in result
        if len(strs) == 1:
            return [strs]

        for str in strs:
            sorted_str = "".join(sorted(str))
            anagrams[sorted_str].append(str)
        return list(anagrams.values())