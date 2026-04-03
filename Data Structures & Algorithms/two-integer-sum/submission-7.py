class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = dict();
        for i, num in enumerate(nums):
            diff = target - num
            if diff in index_map:
                index_map[diff].append(i);
            else:
                index_map[diff] = [i];
            print (diff, index_map[diff])
        for i, num in enumerate(nums):
            if num in index_map:
                print(i,index_map[num][0])
                if i == index_map[num][0]:
                    if len(index_map[num])>1 :
                        j = index_map[num][1];
                        break;
                else:
                    j = index_map[num][0];
                    break;
        return[i,j]
        