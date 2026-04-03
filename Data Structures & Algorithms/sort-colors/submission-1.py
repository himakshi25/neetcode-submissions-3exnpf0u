class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l=0
        mid=l
        r=len(nums)-1
        while mid>=l and mid<=r:
            print (f"{l} {mid} {r}")
            if nums[mid] == 0:
                nums[mid] = nums[l]
                nums[l]=0
                while l<=r and nums[l] == 0:
                    l+=1
                if mid<l:
                    mid=l
            elif nums[mid] == 2:
                nums[mid] = nums[r]
                nums[r]=2
                while l<=r and nums[r] == 2:
                    r-=1
            else:
                mid+=1
            
        