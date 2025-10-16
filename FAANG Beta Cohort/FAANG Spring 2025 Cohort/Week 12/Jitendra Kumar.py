#Fizz Buzz : https://leetcode.com/problems/fizz-buzz/description/
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res

# Time Complexity : O(n) Need to iterate in loop over all elements.
# Space Complexity : O(n) : Need to allocate space for all the n elements



#Integer to Roman : https://leetcode.com/problems/integer-to-roman/description/
class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"),  (90, "XC"), (50, "L"),  (40, "XL"),
        (10, "X"),   (9, "IX"),  (5, "V"),   (4, "IV"), (1, "I")
        ]
        res = ""
        for v, s in val:
            while num >= v:
                res += s
                num -= v
        return res

# Time Complexity : O(1)
# Space Complexity: O(1)
