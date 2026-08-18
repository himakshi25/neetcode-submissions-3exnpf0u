# since we need to find min k where work is done in h hours, for any bigger k it will be automatically completed so only need to consider minimum side. Do binary search on range 1 to maxele in array and on each mid iterate array to check number of hours.
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left,right = 1,max(piles)

        while left<=right:

            mid = left+(right-left)//2

            work=0
            for p in piles:
                work+=math.ceil(p/mid)
            
            if work<=h:
                right = mid-1
            else:
                left = mid+1
        return left


        