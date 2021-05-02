class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<1:
            return 0
        l,r=0,len(height)-1
        lMax=height[l]
        rMax=height[r]
        ret=0
        while l<r:
            if height[l]>lMax:
                lMax=height[l]
            if height[r]>rMax:
                rMax=height[r]
            if lMax<rMax:
                ret+=lMax-height[l]
                l+=1
            else:
                ret+=rMax-height[r]
                r-=1
        return ret
