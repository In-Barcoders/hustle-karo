class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        f, ind = True, 0
        for i in range(len(nums)):
            if f:
                if target > nums[ind]:
                    ind += 1
                elif target == nums[ind]:
                    return ind
                else:
                    ind -= 1
                    f = False
            else:
                if target > nums[ind]:
                    return -1
                elif target < nums[ind]:
                    ind -= 1
                elif target == nums[ind]:
                    return len(nums) + ind
        return -1
