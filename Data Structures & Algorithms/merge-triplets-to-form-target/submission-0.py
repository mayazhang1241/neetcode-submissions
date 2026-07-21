class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # Can only add it to the 'good' triplet set if current triplet has smaller
        # value than target set

        good = set()

        # Skip past values that are greater than target bc they break
        # the upper bound rule
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            # For each number in each triplet, if the value is the same as 
            # the target, add it to the good set
            for i, value in enumerate(t):
                if value == target[i]:
                    good.add(i)

        # If the length of the good set is 3, we found the target triplet
        # in triplets!
        return len(good) == 3
