class Solution:
    # def binarysearch(self, l, r, target, nums:List[int]) -> int:
    #     while(l<=r):
    #         mid = l+(r-l)//2
    #         if target == nums[mid]:
    #             return mid
    #         elif target<nums[mid] :
    #             r=mid-1
    #         else:
    #             l=mid+1
    #     return -1

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while(left<=right):
            mid = left + (right-left)//2
            if (target == nums[mid]):
                return mid
            if nums[left]<=nums[mid] : # if left half is sorted
                if nums[left] <= target <nums[mid]: # if target in sorted
                    right = mid-1
                # res = self.binarysearch(left, mid-1, target, nums)
                # if res!=-1:
                #     return res
                else:
                    left=mid+1
            else: # if right is sorted half
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                # res = self.binarysearch(mid+1, right, target, nums)
                # if res!=-1:
                #     return res
                else:
                    right=mid-1
        return -1


        