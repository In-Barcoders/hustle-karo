class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ls = len(nums) - 1
        for i in range(ls, -1, -1):
            if i + nums[i] >= ls:
                ls = i
        return ls == 0
