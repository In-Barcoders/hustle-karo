class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        index = k-1
        nums = [str(i) for i in range(1, n+1)]
        fact = math.factorial(n)
        output = []

        while nums:
            fact //= len(nums)
            pos = index // fact
            output.append(nums.pop(pos))
            index %= fact
        return ''.join(output)
