class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if trunc(dividend/divisor)>2**31 -1:
            return 2**31 -1
        return trunc(dividend/divisor) 
