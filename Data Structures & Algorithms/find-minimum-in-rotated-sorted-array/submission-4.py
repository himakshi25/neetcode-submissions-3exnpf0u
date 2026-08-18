class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1

        while left<=right:

            mid = left+(right-left)//2

            if mid-1>=0 and nums[mid]<=nums[mid-1]:
                return nums[mid]
            elif nums[left]<=nums[mid]:
                if nums[mid]<nums[right]:
                    right=mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<nums[right]:
                    right=mid-1
                else:
                    left = mid+1

        return nums[mid]