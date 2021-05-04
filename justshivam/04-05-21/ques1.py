class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxnum = nums[0]
        currentmaxnum = nums[0]
        if len(nums) == 1:
            return maxnum
        for i in range(1, len(nums)):
            currentmaxnum = max(nums[i], nums[i]+currentmaxnum)
            if currentmaxnum > maxnum:
                maxnum = currentmaxnum
        return maxnum
