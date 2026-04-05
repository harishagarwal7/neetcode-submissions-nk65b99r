class Solution:
    def countSubstrings(self, s: str) -> int:
        matrix=[]
        n=len(s)
        matrix.append([0]*n)
        matrix[0][0]=1
        for i in range(1,n):
            matrix.append([0]*n)
            matrix[i][i]=1
            if(s[i-1]==s[i]):
                matrix[i-1][i]=1
        #print(matrix)
        for j in range(2,n):
            for i in range(n):
                #print("i"+str(i)+"j"+str(j))
                if(i+j>=n):
                    break
                if(s[i+j]==s[i]):
                    #print("i "+str(i)+"j "+str(j))
                    #print(matrix[i+1][i+j-1])
                    matrix[i][i+j]=matrix[i+1][i+j-1]
        sum1=n
        for i in range(n):
            for j in range(i+1,n):
                sum1+=matrix[i][j]
        #print(matrix)
        return sum1

            