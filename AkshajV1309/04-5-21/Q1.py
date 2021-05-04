class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxE = 0
        maxS = -math.inf
        
        for ele in nums:
            maxE += ele
            if maxS < maxE:
                maxS = maxE
            if maxE < 0:
                maxE = 0
        return maxS
