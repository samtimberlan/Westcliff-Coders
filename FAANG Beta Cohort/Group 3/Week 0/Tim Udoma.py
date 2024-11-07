class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            if num in map:
                return [i, map[num]]

            diff = target - num
            
            map[diff] = i

    # Time complexity O(n)
    # Space complexity O(n)

    def isPalindrome(self, s: str) -> bool:
        # Filter for alphanumeric characters and convert to lowercase
        s_filtered = [x for x in s.lower() if x.isalnum()]
        
        # Compare the list with its reverse
        return s_filtered == s_filtered[::-1]

    # Time complexity O(n)
    # Space complexity O(n)
        