class MinStack:

    # two stacks
    # stack: stores all pushed values
    # minStack: stores the minimum so far at each level

    def __init__(self):
        self.stack = []
        self.minStack = []


    def push(self, val: int) -> None:
        # push val onto stack
        # compare with current minimum on minStack
        # whichever one is smaller, push that onto minStack

        self.stack.append(val)

        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
