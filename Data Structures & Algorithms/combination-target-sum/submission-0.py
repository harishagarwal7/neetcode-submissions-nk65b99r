class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr=[[]]
        arr1=[0]
        arr2=[-1]
        ans=[]
        while(len(arr)!=0):
            ind=arr2[0]
            s=arr1[0]
            array=arr[0]
            arr.remove(array)
            arr1.remove(s)
            arr2.remove(ind)
            for i in range(ind+1,len(nums)):
                j=1
                while(s+(nums[i]*j)<target):
                    arr.append(array+([nums[i]]*j))
                    arr1.append(s+(nums[i]*j))
                    arr2.append(i)
                    j+=1
                if(s+(nums[i]*j)==target):
                    ans.append(array+([nums[i]]*j))
        return ans

        