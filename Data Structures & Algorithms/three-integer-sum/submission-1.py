class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=[]
        hm={}
        for i in range(len(nums)):
            hm[nums[i]]=i
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(-(nums[i]+nums[j]) in hm and hm[-(nums[i]+nums[j])]>j):
                    l=[nums[i],nums[j],-(nums[i]+nums[j])]
                    l.sort()
                    if(l not in s):
                        s.append(l)
        return s
        