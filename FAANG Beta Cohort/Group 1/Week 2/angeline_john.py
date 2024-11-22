"""
    ADD ajohn 20241121 - solution to the 155. Min Stack leet code problem
"""

# 155. Min Stack leet code problem
class MinStack:
    stk = []

    # constructor
    def __init__(self):
        self.data = []    

    
    # function to push element into the stack
    def push(self, val: int) -> None:
        MinStack.stk.append(val)
        
    
    # function to remove the top element in the stack
    def pop(self) -> None:
        MinStack.stk.pop()
        
    
    # function to retrieve the top element in the stack
    def top(self) -> int:
        return MinStack.stk[-1]
        
    
    # function to return the minimum element in the stack
    def getMin(self) -> int:
        return min(MinStack.stk)