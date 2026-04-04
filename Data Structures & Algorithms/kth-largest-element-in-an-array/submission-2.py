import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for i in range(len(nums)):
            if i >= k:
                ele=heapq.heappop(res)
                if ele<nums[i]:
                    heapq.heappush(res,nums[i])
                else:
                    heapq.heappush(res,ele)
            else:
                heapq.heappush(res,nums[i])
        print(res)
        return heapq.heappop(res)
        