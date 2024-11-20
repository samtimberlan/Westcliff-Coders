# Leetcode 155.Min Stack
class MinStack:
    
    def __init__(self):
        # Initialize an empty list to store the elements and their corresponding minimum values
        self.stack = []
    
    def getMin(self) -> int:
        # Return the current minimum value, which is the second element of the top list in the stack
        # If the stack is empty, return None
        return self.stack[-1][1] if self.stack else None

    def push(self, value: int) -> None:
        # Retrieve the current minimum value (if stack is empty, it returns None)
        current_min = self.getMin()
        
        # If the stack is empty or the current value is smaller than the current minimum, update the minimum
        if current_min == None or current_min > value:
            min_val = value
            
        # Append the value and the updated minimum to the stack
        self.stack.append([value, min_val])
    
    def pop(self) -> None:
        # Pop the top element of the stack, which removes both the value and the associated minimium
        self.stack.pop()
    
    def top(self) -> int:
        # Return the value of the top element of the stack. If the stack is empty return None
        return self.stack[-1][0] if self.stack else None
    
    
    
# Leetcode 899.Orderly Queue
class Solution:
    
    def orderlyQueue(self, string: str, k: int) -> str:
        # If k > 1, sort the string and return it as sorted order gives the lexicographically smallest result
        if k > 1:
            return ''.join(sorted(string))
        
        # Initialize 'min_string' to store the lexicographically smallest rotation of the string
        min_string = string
        
        # Loop through each possible rotation of the string
        for i in range(1, len(string)):
            # Calculate the rotated string and update 'min_string'
            min_string = min(min_string, string[i:] + string[:i])
            
        # Return the lexicographically smallest string found
        return min_string