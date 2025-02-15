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
    

# 2.
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Calculate arrival times in-place to save memory
        for i in range(len(dist)):
            # ceiling division
            '''
            dist = 7, speed = 3
            Regular: 7/3 = 2.333... -> ceil(2.333...) = 3
            Formula: (7-1)//3 + 1 = 6//3 + 1 = 2 + 1 = 3
            '''
            dist[i] = (dist[i] - 1) // speed[i] + 1
            
        # Sort in-place
        dist.sort()
        
        # Check each minute
        for i in range(len(dist)):
            if dist[i] <= i:
                return i
                
        return len(dist)