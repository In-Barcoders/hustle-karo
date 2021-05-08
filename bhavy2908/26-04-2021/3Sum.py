class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        n = len(nums)
        for i in range(n):
            j, k = i+1, n-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j, k = j+1, k-1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1
        return list(result)