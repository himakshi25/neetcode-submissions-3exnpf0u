class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr = 1 
        zero = 0
        for num in nums:
            if num == 0: 
                zero += 1
            else:
                pr = pr * num
        if zero>1:
            return [0]*len(nums)
        for i, num in enumerate(nums):
            if num == 0:
                ar = [0]*len(nums)
                ar[i] = pr
                return ar
            nums[i] = int(pr/nums[i])
        
        return nums

        