class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        matrix=[]
        for i in range(n):
            matrix.append([0]*n)
        #print (matrix)
        matrix[0][0]=1
        maxDiff=1
        word=str(s[0])
        for i in range(1,n):
            matrix[i][i]=1
            if(s[i]==s[i-1]):
                matrix[i-1][i]=1
                maxDiff=2
                word=s[i-1:i+1]
        for j in range(2,n):
            for i in range(n):    
                if(i+j>=n):
                    break
                #print("i"+str(i)+"j"+str(j))
                if(s[i]==s[i+j] and matrix[i+1][i+j-1]==1):
                    matrix[i][i+j]=1
                    if(j+1>maxDiff):
                        word=s[i:i+j+1]
        #print(matrix) 
        return word