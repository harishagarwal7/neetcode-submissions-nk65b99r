class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm={}
        for i in range (len(nums)):
            hm[nums[i]]=1
        maxj=0
        for i in range (len(nums)):
            if (nums[i]-1 not in hm):
                j=1
                while((nums[i]+j) in hm):
                    j+=1
                maxj=max(maxj,j)
        return maxj