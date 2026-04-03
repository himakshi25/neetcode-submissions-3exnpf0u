class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for item in strs:
            s = "".join(sorted(item))
            mp[s].append(item)

        return list(mp.values())