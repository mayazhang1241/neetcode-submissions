class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

       # Brute force - start at index and simulate process, return
       # end index after 1 full circuit

        # n = len(gas)

        # for i in range(n):
        #     tank_amt = gas[i] - cost[i] 

        #     if tank_amt < 0:
        #         continue

        #     j = (i + 1) % n

        #     while j != i:
        #         tank_amt += gas[j]
        #         tank_amt -= cost[j]

        #         if tank_amt < 0:
        #             break

        #         j += 1
        #         j %= n

        #     if j == i:
        #         return i

        # return -1

        # Greedy solution - Calculate total tank amount at each index,
        # if total < 0, then move onto next index

        # Checks if there is even enough gas to complete the trip
        if sum(gas) < sum(cost):
            return -1

        total = 0
        result = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                result = i + 1

        return result


        
    