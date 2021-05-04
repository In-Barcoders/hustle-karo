class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def rec(cur):
            if len(cur) >= l:
                res.append(cur)
                return
            for i in nums:
                if i in cur:
                    continue
                rec(cur+[i])
        res = []
        l = len(nums)
        rec([])
        return res
