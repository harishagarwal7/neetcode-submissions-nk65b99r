class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            h[nums[i]]=i
        for i in range(len(nums)):
            if(2*nums[i]==target):
                if(h[nums[i]]!=i):
                    return [i,h[nums[i]]]
            elif target-nums[i] in h:
                return [i,h[target-nums[i]]]