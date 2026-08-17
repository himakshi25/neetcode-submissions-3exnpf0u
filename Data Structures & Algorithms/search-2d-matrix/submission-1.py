# apply binary search on col 0 first and find now no. then on that row do binary search

class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        rl=len(m)
        cl = len(m[0])
        left = 0
        right = rl-1

        rowforbinsearch = -1
        if target>= m[right][0]:
            rowforbinsearch=right
        while left<right:
            mid = left + (right-left)//2
            if target == m[mid][0]:
                return True
            elif target>m[mid][0]:
                left = mid+1
            else:
                right = mid
        if rowforbinsearch == -1:
            rowforbinsearch = left-1
        if rowforbinsearch < 0:
            return False

        left = 0
        right = cl-1
        while left<=right:
            mid = left + (right-left)//2
            if target == m[rowforbinsearch][mid]:
                return True
            elif target>m[rowforbinsearch][mid]:
                left = mid+1
            else:
                right = mid-1
        return False        