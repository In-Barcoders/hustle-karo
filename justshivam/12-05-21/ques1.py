class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        st = [1, 2]
        while len(st) < n:
            st.append(st[-1]+st[-2])
        return st[-1]
