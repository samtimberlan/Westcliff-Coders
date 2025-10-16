class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)
    
    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Time Complexity: Push and Empty are O(1) but pop and peek are amortized O(1) because the stack_out is only used when the stack_out is empty.
# Space Complexity: O(n) because the elements are stored across stack_in and stack_out, utilizing linear space relative to the number of elements.


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0  # Index for popped sequence

        for x in pushed:
            stack.append(x)  # Push x onto the stack
            # While the stack is not empty and the top matches popped[i]
            while stack and stack[-1] == popped[i]:
                stack.pop()  # Pop from the stack
                i += 1  # Move to the next element in popped

        # If the stack is empty, all elements were matched correctly
        return not stack
    
# Time Complexity: O(n) becaus the algorithm processes each element in the pushed sequence exactly once
# Space Complexity: O(n) the auxiliary stack used for simulation may store up to n elements in the worst case,