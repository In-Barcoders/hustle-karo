class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums) - 1
        for j in range(l - 1, -1, -1):
            if j + nums[j] >= l:
                l = j
                
        if l == 0:
            return True
        return False
