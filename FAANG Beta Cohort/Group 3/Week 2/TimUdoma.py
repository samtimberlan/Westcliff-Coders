class Solution:
    def isValid(self, s: str) -> bool:
        # trav. add to stack if ( and stack. keep map. pop. check if match. ret 
        if not s:
            return True

        stack = deque()
        map = {'(': ')', '[': ']', '{': '}'}

        for c in s:

            if c in map:
                stack.append(c) # opening bracket
            else:
                if not stack: return False # no matching closing bracket
                prev = stack.pop() 
                if map[prev] != c: return False

        return not stack
        