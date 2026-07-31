class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for st in strs:
            sortedst = "".join(sorted(st))
            mp[sortedst].append(st)

        return list(mp.values())
            