class Solution:
    def plusOne(self, arr: List[int]) -> List[int]:
        if arr[-1] == 9:
            i = 1
            while i <= len(arr):
                if arr[-i] == 9:
                    arr[-i] = 0
                else:
                    arr[-i] += 1
                    return arr
                i += 1
            return [1] + arr
        arr[-1] += 1
        return arr
