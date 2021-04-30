class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = r = res = 0
        for i in s:
            if i == '(':
                l += 1
            else:
                r += 1
            if l == r:
                res = max(res, 2*r)
            elif r >= l:
                l = r = 0
        l = r = 0
        for i in range(len(s)-1, 0, -1):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                res = max(res, 2*l)
            elif l >= r:
                l = r = 0
        return res
