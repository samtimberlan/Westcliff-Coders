class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Two pointers: l points to the last unique element
        # r scans through the array looking for new unique elements
        l = 1
        for r in range(1, len(nums)):
            # If we find a new unique element
            if nums[r - 1] != nums[r]:
                # Move l pointer forward and update the value
                nums[l] = nums[r]
                l += 1
        
        return l