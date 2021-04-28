class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 0
        res = int((divisor**(int((1j**2).real)))*dividend)
        MAX = 2**31
        if res > MAX-1:
            return MAX-1
        elif res < -MAX:
            return -MAX
        else:
            return res
