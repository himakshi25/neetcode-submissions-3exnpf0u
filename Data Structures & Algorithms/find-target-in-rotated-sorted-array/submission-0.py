class Solution:
    def binarysearch(self, l, r, target, nums:List[int]) -> int:
        while(l<=r):
            mid = l+(r-l)//2
            if target == nums[mid]:
                return mid
            elif target<nums[mid] :
                r=mid-1
            else:
                l=mid+1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while(left<=right):
            mid = left + (right-left)//2
            if (target == nums[mid]):
                return mid
            if nums[left]<nums[mid] : 
                res = self.binarysearch(left, mid-1, target, nums)
                if res!=-1:
                    return res
                left=mid+1
            else:
                res = self.binarysearch(mid+1, right, target, nums)
                if res!=-1:
                    return res
                right=mid-1
        return -1


        