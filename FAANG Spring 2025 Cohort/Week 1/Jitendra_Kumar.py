#Remove Duplicates from Sorted Array : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0;
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        count += 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
        return count
# Time Complexity : O(n)
# Space Complexity : O(1)

#Eliminate Maximum Number of Monsters : https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival = []
        for i in range(len(dist)):
            arrival.append(dist[i] / speed[i])
        arrival.sort()
        ans = 0
        for i in range(len(arrival)):
            if arrival[i] <= i:
                break
            ans += 1
        return ans
# Time Complexity : O(nlogn)
# Space Complexity : O(n)
