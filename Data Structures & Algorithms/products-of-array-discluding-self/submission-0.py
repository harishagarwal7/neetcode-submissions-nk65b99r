class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd=[1]
        rightProd=[1]
        n=len(nums)
        ans=[]
        for i in range(len(nums)-1):
            leftProd.append(leftProd[i]*nums[i])
            rightProd.append(rightProd[i]*nums[n-1-i])
        for i in range(n):
            ans.append(leftProd[i]*rightProd[n-1-i])
        return ans