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
    
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        
        # Count character frequencies
        char_count = Counter(s)
        
        # Check characters in original order 
        for idx, char in enumerate(s):
            if char_count[char] == 1:
                return idx
                
        return -1
        