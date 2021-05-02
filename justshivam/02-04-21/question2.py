class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        res = start = 0
        for i in range(l):
            if height[i] > 0 and start <= i:
                start = i
                if start == l - 1:
                    break
                end = -1
                for j in range(start+1, l):
                    if height[j] >= height[start]:
                        end = j
                        break
                if end == -1:
                    m = start+1
                    for j in range(start+1, l):
                        if height[j] > height[m]:
                            m = j
                    end = m
                com = start
                if height[end] < height[start]:
                    com = end
                for j in range(start+1, end):
                    res += height[com] - height[j]
                start = end

        return res
