class Solution:
    def isPalindrome(self, s: str) -> bool:
        news=[]
        for i in range(len(s)):
            ordval=ord(s[i])
            if(ordval-ord('a')>=0 and ordval-ord('a')<=26):
                news.append(ordval-ord('a'))
            elif(ordval-ord('A')>=0 and ordval-ord('A')<=26):
                news.append(ordval-ord('A'))
            elif(ordval-ord('0')>=0 and ordval-ord('0')<=9):
                news.append(ordval-ord('9'))
            else:
                continue
        print(news)
        i=0;
        j=len(news)-1
        while(i<j):
            if(news[i]!=news[j]):
                return False
            i+=1
            j-=1
        return True
        