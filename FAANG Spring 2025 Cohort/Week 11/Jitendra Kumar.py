#Single Number : https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

# Time Complexity : O(n) because need to check every number.
# Space Complexity : O(1) : No extra space



#Sum of Two Integers : https://leetcode.com/problems/sum-of-two-integers/
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        MASK = 0xFFFFFFFF
        
        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK
        
        return a if a <= MAX else ~(a ^ MASK)

# Time Complexity : O(1)
# Space Complexity: O(1)
