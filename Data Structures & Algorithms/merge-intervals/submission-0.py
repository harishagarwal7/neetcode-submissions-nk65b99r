class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        start=intervals[0][0]
        end=intervals[0][1]
        ans=[]
        for i in range(len(intervals)):
            if(intervals[i][0]<=end):
                end=max(end,intervals[i][1])
            else:
                ans.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
        ans.append([start,end])
        return ans
