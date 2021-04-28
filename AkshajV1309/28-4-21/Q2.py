class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if int(dividend*(divisor**(-1)))>2**31 -1:
            return 2**31 -1
        return int(dividend*(divisor**(-1)))
