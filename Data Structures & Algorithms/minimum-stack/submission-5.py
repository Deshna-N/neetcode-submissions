class MinStack:

    def __init__(self): 
        self.stack = []
        self.newstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.newstack:
            self.newstack.append(val)
        else:    
            self.newstack.append(min(val, self.newstack[-1]))
            # if self.newstack[-1] < val:
            #     self.newstack.append(self.newstack[-1])
            # elif (self.newstack[-1] > val) or (self.newstack[-1] == val):
            #     self.newstack.append(val)
        
        
    def pop(self) -> None:
        self.stack.pop()
        self.newstack.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        ## so stack has 5, if newstack empty then push
        ## stack now has 5,2 and compare newstack.top with 2, if smaller than pop and add 2 else continue
        ## and when popping from stack then pop from newstack which always got 1 val
        return self.newstack[-1]
            





        # self.small = float('inf')
        # for i in self.stack:
        #     self.small = min(i, self.small)
        # return self.small
        
