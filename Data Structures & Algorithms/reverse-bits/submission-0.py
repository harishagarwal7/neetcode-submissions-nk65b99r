class Solution:
    def reverseBits(self, n: int) -> int:
        s1=bin(n)
        print(s1)
        s="0"*(34-len(s1))
        for i in range(2,len(s1)):
            s=s1[i]+s
        return int(s,2)
        