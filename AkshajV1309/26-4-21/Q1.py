class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=strs
        if len(s) == 0:
            return ""
        c=s[0]
        for i in range(1,len(s)):
            a=""
            if len(c)==0:
                break
            for j in range(len(s[i])):
                if j<len(c) and c[j] == s[i][j]:
                    a+=c[j]
                else:
                    break
            c=a
        return c

