class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = defaultdict(list)
        
        for i, num in enumerate(nums):
            num1 = target-num
            if num1 in hm:
                return [hm.get(num1), i]
            hm[num]=i

        