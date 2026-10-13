class Solution:
    def backtrack(self, nums, remaining, start, path):
        if remaining<0:
            return
        if remaining == 0:
            self.ans.append(path[:])
            return

        for i in range(start, len(nums)):
            if i>start and nums[i] == nums[i-1]:
                continue
            if remaining<nums[i]:
                return
            path.append(nums[i])
            self.backtrack(nums, remaining-nums[i], i+1, path)
            path.pop()


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans=[]
        self.backtrack(sorted(candidates), target, 0, [])

        return self.ans
        
        