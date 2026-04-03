class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mp = defaultdict(list)

        # for item in strs:
        #     s = "".join(sorted(item))
        #     mp[s].append(item)

        # return list(mp.values())

        mp = defaultdict(list)
        for item in strs:
            key = [0]*26
            for char in item:
                key[ord(char) - ord('a')] += 1
            mp[tuple(key)].append(item)
            
        return list(mp.values())