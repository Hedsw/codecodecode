class MinStack:
    def __init__(self):

        self.datas = []
        
    def push(self, x: int) -> None:
        m = x
        if self.datas:
            m = self.datas[-1][-1]
            if m > x:
                m = x 
        self.datas.append((x,m))

    def pop(self) -> None:
        self.datas.pop()
        
    def top(self) -> int:


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
    
    def push(self, x: int) -> None:
        m = x
        if self.nums:
            m = self.nums[-1][1]
            if m > x:
                m = x
        self.nums.append((x,m))

    def pop(self) -> None:
        self.nums.pop()

    def top(self) -> int:
        return self.nums[-1][0]

    def getMin(self) -> int:
        return self.nums[-1][1]
 '''
 Second Solution : 
'''
 class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        self.minValue = self.stack[:]
        self.minValue = min(self.minValue)
        return self.minValue


'''
Third Solution

'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        #print(self.stack)
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int: 
        return self.stack[-1]
    
    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()