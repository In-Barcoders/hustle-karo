class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        O=[]
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j<k:
                if k<len(nums)-1 and nums[k]==nums[k+1]:
                    k-=1
                    continue
                if nums[i]+nums[j]+nums[k]>0:
                    k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    O.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
        return O
