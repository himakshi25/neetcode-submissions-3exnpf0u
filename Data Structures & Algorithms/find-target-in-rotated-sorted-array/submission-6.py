class Solution:
    def binsearch(self, nums, target, left, right):
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                return mid
            elif target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return -1

    def search(self, nums: List[int], target: int) -> int:

        left,right = 0,len(nums)-1

        while left<=right:
            mid = left+(right-left)//2

            if nums[mid] == target:
                return mid
            elif nums[left]<=nums[mid]:
                if target>=nums[left] and target<nums[mid]:
                    return self.binsearch(nums,target,left,mid)
                else:
                    left = mid+1
            else:
                if target>nums[mid] and target<=nums[right]:
                    return self.binsearch(nums,target,mid,right)
                else:
                    right = mid-1
        return -1
        