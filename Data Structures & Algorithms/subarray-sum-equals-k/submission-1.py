class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum=0
        prefixmap = defaultdict(int)
        count=0
        for num in nums:
            prefixsum += num
            if prefixsum-k == 0:
                count+=1
            if prefixsum-k in prefixmap:
                count+=prefixmap[prefixsum-k]
            prefixmap[prefixsum]+=1
        return count

        