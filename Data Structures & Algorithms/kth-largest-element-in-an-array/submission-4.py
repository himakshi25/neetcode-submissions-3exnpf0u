class Solution:
    def partition(self, arr: List[int], low, high) -> int:
        pivot = arr[high]
        i = low - 1  # Index of the smaller element
        
        for j in range(low, high):
            # If the current element is smaller than or equal to the pivot
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap elements
                
        # Place the pivot in its correct sorted position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1  # Return the partitioning index


    def quicksort(self, nums: List[int], findindex, start, end):
        if start<end:
            pi = self.partition(nums, start, end)
            
            if pi == findindex:
                return
            
            if findindex>pi:
                return self.quicksort(nums, findindex, pi+1, end)
            else:
                return self.quicksort(nums, findindex, start, pi-1)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quicksort(nums, len(nums)-k, 0, len(nums)-1)
        return nums[len(nums)-k]
        
        