class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s=len(nums)
        ar = [[] for _ in range(s+1)]

        mp = Counter(nums)

        for key,v in mp.items():
            ar[v].append(key);
        
        ans = []
        for val in ar[::-1]:
            if len(val)!=0:
                if len(val)<=k:
                    ans.extend(val)
                    k=k-len(val)
                    if k==0: break;
                else:
                    ans.extend(val[:k])
                    break
        return ans;

