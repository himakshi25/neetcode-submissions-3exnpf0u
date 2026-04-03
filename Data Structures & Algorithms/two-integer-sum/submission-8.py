class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        ar =[]
        for i, num in enumerate(nums):
            diff = target-num
            print(diff)
            if diff in hm:
                return [hm[diff], i]
                break
            hm[num]=i
