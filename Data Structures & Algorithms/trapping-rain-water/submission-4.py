# move left to right and find max till element and then do max-element. same right to left and do sum of mini of both array

# optimised: 2 pointer 

class Solution:
    def trap(self, height: List[int]) -> int:
        # left = [0]*len(height)
        # right = [0]*len(height)
        # l=0
        # r=len(height)-1
        # maxl=0
        # while l<len(height):
        #     maxl=max(maxl,height[l])
        #     left[l]=maxl-height[l]
        #     l+=1
        # maxr=0
        # while r>=0:
        #     maxr=max(maxr,height[r])
        #     right[r]=maxr-height[r]
        #     r-=1
        # sum=0
        # for i in range(len(height)):
        #     sum+=min(left[i],right[i])
        # return sum
        leftmax,rightmax,water,left=0,0,0,0
        right=len(height)-1
        while left < right : 
            if height[left] < height[right]:
                if leftmax > height[left]:
                    water += leftmax-height[left]
                else:
                    leftmax=height[left]
                left+=1
            else:
                if rightmax > height[right]:
                    water += rightmax-height[right]
                else:
                    rightmax=height[right]
                right-=1
        return water

        