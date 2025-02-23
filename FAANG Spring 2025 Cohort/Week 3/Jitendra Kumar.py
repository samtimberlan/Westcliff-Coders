#Implement Queue using Stacks: https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:
    def __init__(self):
        self.stackIn = []
        self.stackOut = []
        
    def move_in_to_out(self) -> None:
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())

      def push(self, x: int) -> None:
        self.stackIn.append(x)
        
    def pop(self) -> int:
        self.move_in_to_out()
        return self.stackOut.pop()

    def peek(self) -> int:
        self.move_in_to_out()
        return self.stackOut[-1]

    def empty(self) -> bool:
        return not self.stackIn and not self.stackOut
        
# MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Test for Implement Queue using Stacks
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())  # Output: 1
print(queue.pop())   # Output: 1
print(queue.empty()) # Output: False

# Time Complexity : Amortized O(1) for all operations.
# Space Complexity : Two stacks (stack_in and stack_out) store at most n elements.

#Validate Stack Sequences: https://leetcode.com/problems/validate-stack-sequences/
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_index = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        return not stack

# Test for Validate Stack Sequences
print(validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))  # Output: True
print(validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))  # Output: False

# Time Complexity : O(n) because each element is pushed and popped at most once, resulting in a total time complexity of O(n).
# Space Complexity : O(n) since the auxiliary stack holds at most O(n) elements, with no extra data structures apart from integer counters..
