class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    # found this method form the internet
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        listSize = len(nums)

        for i in range(listSize):
            needNum = target - nums[i]
            if needNum in numMap:
                return [numMap[needNum], i]
            numMap[nums[i]] = i
