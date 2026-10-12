class Solution:
    def backtrack(self, nums, remaining, start, path):
        if remaining<0:
            return
        if remaining == 0:
            self.ans.append(path[:])
            return

        for i in range(start, len(nums)):
            if remaining<nums[i]:
                return
            path.append(nums[i])
            self.backtrack(nums, remaining-nums[i], i, path)
            path.pop()


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans=[]
        self.backtrack(sorted(nums), target, 0, [])

        return self.ans
        