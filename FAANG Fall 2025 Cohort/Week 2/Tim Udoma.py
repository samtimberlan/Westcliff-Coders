class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)


'''
        Original:  [1, 2, 3, 4, 5, 6, 7]
                    ↓  ↓  ↓  ↓  ↓  ↓  ↓
        Reversed:  [7, 6, 5, 4, 3, 2, 1]
```

**What happened?** 
- The last 3 elements (5,6,7) are now at the front, but **backwards** ❌
- The first 4 elements (1,2,3,4) are at the back, also **backwards** ❌

---

### **Step 2: Reverse the first K elements**
```
Current:   [7, 6, 5, | 4, 3, 2, 1]
            ↓  ↓  ↓
Reverse:   [5, 6, 7, | 4, 3, 2, 1]
```

**What happened?**
- First 3 elements are now correct! ✅
- But the rest are still backwards ❌

---

### **Step 3: Reverse the remaining elements**
```
Current:   [5, 6, 7, | 4, 3, 2, 1]
                       ↓  ↓  ↓  ↓
Final:     [5, 6, 7, | 1, 2, 3, 4] ✅
```

**Perfect!** Everything is now in the right order.

---
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # stack prob
        # pop from back while k > 0. append

        n = len(nums)
        if n == 0:
            return
        k %= n # avoid unnecessary rotations

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n-1) #flip everything
        reverse(0, k-1) #straighten first part
        reverse(k, n-1) #straighten last part

        

        