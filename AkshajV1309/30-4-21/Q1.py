class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        O,count=[-1],0
        for i in range(len(s)):
            if s[i]=='(':
                O.append(i)
            else:
                O.pop()
                if not O:
                    O.append(i)
                else:
                    count=max(count,i-O[-1])
        return count
