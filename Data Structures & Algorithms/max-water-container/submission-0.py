class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxi = float("-inf")
        while i<j:
            maxi = max(min(heights[i], heights[j])*(j-i), maxi)
            if heights[i] < heights[j]:
                i+=1
            elif heights[i] > heights[j]:
                j-=1
            else:
                i+=1
                j-=1
        return maxi


        