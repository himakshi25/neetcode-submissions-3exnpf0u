class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s=len(nums)
        ar = [[] for _ in range(s+1)]

        mp = Counter(nums)
        print(mp)

        for key,v in mp.items():
            ar[v].append(key);

        print(ar)
        
        ans = []
        for val in ar[::-1]:
            if len(val)!=0:
                print(val,k)
                if len(val)<=k:
                    ans.extend(val)
                    k=k-len(val)
                else:
                    ans.extend(val[:k])
                    k=0
                if k==0:
                    break;
        return ans;

