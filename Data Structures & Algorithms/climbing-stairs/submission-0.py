class Solution:
    def climbStairs(self, n: int) -> int:

        # keep track of prev 2 variables
        # update one and two variable as you iterate backwards
        
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one