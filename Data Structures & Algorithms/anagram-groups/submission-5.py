class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # use a dict
        # key : value
        # frequencies of each letter sorted alphabetically : list of words that correspond
        # [a: 1, h: 1, t: 1] : ["hat"]
        # [a: 1, c: 1, t: 1] : ["act", "cat"]
        # [o: 1, p: 1, s: 1, t: 1] : ["stop", "pots", "tops"]

        anagrams = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            anagrams[sorted_s].append(s)

        return list(anagrams.values())