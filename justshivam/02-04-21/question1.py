class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
        n1 = n2 = cur = 0
        for i in range(len(num1)-1, -1, -1):
            n1 += (dic[num1[i]])*(10**cur)
            cur += 1
        cur = 0
        for i in range(len(num2)-1, -1, -1):
            n2 += (dic[num2[i]])*(10**cur)
            cur += 1
        return str(n1*n2)
