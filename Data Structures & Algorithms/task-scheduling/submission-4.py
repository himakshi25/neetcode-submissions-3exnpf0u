# tasks = ["A","A","A","B","B","B","C"], n = 2
# We have:

# A: 3 times
# B: 3 times
# C: 1 time
# Cooldown: 2 (need 2 slots between same tasks)


# Step 1: Identify the Bottleneck
# "Both A and B appear 3 times (max frequency). They're the constraint."

# Step 2: Visualize the Pattern
# "Let me think about A's skeleton with cooldown n=2:"
# A _ _ A _ _ A
# This is (3-1) = 2 groups of (2+1) = 3 slots, plus the final A.
# Same for B:
# A _ _ A _ _ A
# "Now I can fill the gaps with other tasks. Let me place B and C:"
# A B C A B _ A B
# 0 1 2 3 4 5 6 7
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = Counter(tasks)
        max_freq = max(hm.values())

        max_num_with_same_freq = list(hm.values()).count(max_freq)
        total_count = (max_freq-1)*(n+1) + max_num_with_same_freq

        return max(total_count, len(tasks))