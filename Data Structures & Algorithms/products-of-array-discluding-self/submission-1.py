class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prevpr = nums[0]
        out = [1] * len(nums)
        for i in range(1, len(nums)):
            out[i] = prevpr
            prevpr = prevpr * nums[i]
        # print(out)
        prevpr = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            out[i] = out[i] * prevpr
            # print(out[i])
            prevpr = prevpr * nums[i]
        # print(out)
        return out

        