class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        l=[]
        for s in strs:
            hm={}
            for char in s:
                if char in hm:
                    hm[char]+=1
                else:
                    hm[char]=1
            if hm in l:
                ind=l.index(hm)
                h[strs[ind]].append(s)
            else:
                h[s]=[]
                h[s].append(s)
            l.append(hm)
        return (list(h.values()))