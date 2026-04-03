#from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    
        mp = Counter(nums)
        #print(mp)
        for index, value in mp.items():
            #print(index,value)
            if value>1:
                return True
        return False