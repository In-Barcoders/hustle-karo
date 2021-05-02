class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=n2=0
        n=num1+num2
        for i in range(len(n)):
            if i<len(num1):
                n1+=(ord(n[i])-48)*10**(len(num1)-i-1)
            else:
                n2+=(ord(n[i])-48)*10**(len(n)-i-1)
        return str(n1*n2)
