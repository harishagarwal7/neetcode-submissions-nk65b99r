class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm1={}
        hm2={}
        for num in nums:
            if num in hm1:
                old=hm1[num]
                hm1[num]+=1
                hm2[old].remove(num)
                if(len(hm2[old])==0):
                    hm2.pop(old)
                if(old+1 not in hm2):
                    hm2[old+1]=[]
                hm2[old+1].append(num)
            else:
                hm1[num]=1
                if 1 not in hm2:
                    hm2[1]=[]
                hm2[1].append(num)
        print(hm2)
        l=list(hm2.keys())
        l.sort()
        ans=[]
        i=len(l)-1
        while(len(ans)<k):
            ans+=hm2[l[i]]
            i-=1
        return ans