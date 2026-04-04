class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr=[-1]*(amount+1)
        arr[0]=0
        for coin in coins:
            if coin<=amount:
                arr[coin]=1
        for i in range(amount+1):
            if(arr[i]!=-1):
                continue
            minimum=amount+2
            #print("i"+str(i))
            for j in coins:
                if (i-j>=0 and arr[i-j]!=-1):
                    minimum=min(minimum,arr[i-j]+1)
            if(minimum!=amount+2):
                arr[i]=minimum
        #print(arr)
        return arr[amount]



        