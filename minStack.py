class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.item = []

    def push(self, x: int) -> None:
        self.item.append(x)

    def pop(self) -> None:
        return self.item.pop()

    def top(self) -> int:
        return self.item[len(self.item) - 1]

    def getMin(self) -> int:
        return min(self.item)

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.item = []
        self.minStack = []
    def push(self, x: int) -> None:
        self.item.append(x)
        if self.minStack:
            x = min(x, self.minStack[-1])
        self.minStack.append(x)

    def pop(self) -> None:
        
        if len(self.item) == 0:
            return 
        else:
            self.minStack.pop()
            self.item.pop()

    def top(self) -> int:
        return self.item[len(self.item) - 1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
