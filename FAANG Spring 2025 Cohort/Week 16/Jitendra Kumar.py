#First Bad Version : https://leetcode.com/problems/first-bad-version/description
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Time Complexity : O(log n) because of searching only half the element in every step in binary search
# Space Complexity : O(1) because need to allocate space only for lefr, right and mid


#Search in Rotated Sorted Array : https://leetcode.com/problems/search-in-rotated-sorted-array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

# Time Complexity : O(log n) because of searching only half the element in every step in binary search
# Space Complexity: O(1) because need to allocate space only for lefr, right and mid
