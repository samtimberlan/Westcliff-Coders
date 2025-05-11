#House Robber : https://leetcode.com/problems/house-robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0,0
        for num in nums:
            curr = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = curr
        return prev1

# Time Complexity : O(n) Need to iterate in loop over all elements.
# Space Complexity : O(1) : Need to allocate space only for 3 variables


#Coin Change : https://leetcode.com/problems/coin-change
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

# Time Complexity : O(num coins * amount) Need to iterate over all coins and all amount
# Space Complexity: O(amount) space required for dp list of size amount
