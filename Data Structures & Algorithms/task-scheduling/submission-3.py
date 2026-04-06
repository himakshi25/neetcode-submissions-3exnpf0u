class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = Counter(tasks)
        max_freq = max(hm.values())

        max_num_with_same_freq = list(hm.values()).count(max_freq)
        total_count = (max_freq-1)*(n+1) + max_num_with_same_freq

        return max(total_count, len(tasks))