"""
    ADD ajohn 20241121 - solution to the 155. Min Stack leet code problem
"""

# 155. Min Stack leet code problem
class MinStack():
    # constructor
    def __init__(self):
        self.stack = []
        self.minStack = []
    

    # function to push an element to the stack
    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)


    # function to remove the element on top of the stack
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    
    # function to get the top element of the stack
    def top(self) -> int:
        return self.stack[-1]
    


    # function to retrieve the minimum element in the stack
    def getMin(self) -> int:
        return self.minStack[-1]