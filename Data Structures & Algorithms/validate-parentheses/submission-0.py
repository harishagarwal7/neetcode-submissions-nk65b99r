class Solution:
    def isValid(self, s: str) -> bool:
        h={
            '}':'{',
            ')':'(',
            ']':'['
        }
        l=[]
        for char in s:
            if char in h.values():
                l.append(char)
            else:
                ch1=h[char]
                if(len(l)==0):
                    return False
                popchar=l.pop()
                if(popchar!=ch1):
                    return False
        if(len(l)==0):
            return True
        else:
            return False
