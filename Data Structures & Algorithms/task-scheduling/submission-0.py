import heapq
from collections import deque


class Solution:
    """
    Hash Map
    The task that should be processed first is the task with
    the highest frequency because of the constraint where identical
    tasks must be separated by at least `n` CPU cycles, to cooldown
    the CPU. So in between the cooldown, you would want to put the
    second highest task frequency and so on so that we reduce the
    amount of times that the CPU is idle.
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_hash_map = {}

        for task in tasks:
            if task in tasks_hash_map:
                tasks_hash_map[task] += 1
            else:
                tasks_hash_map[task] = 1

        cpu_cycles = 0
        max_heap = [-frequency for char, frequency in tasks_hash_map.items()]
        heapq.heapify(max_heap)
        queue = deque()

        while max_heap or queue:
            cpu_cycles += 1
            unlock_time = cpu_cycles + n

            if max_heap:
                frequency = heapq.heappop(max_heap)
                frequency += 1

                if frequency != 0:
                    queue.append((frequency, unlock_time))
            
            if queue and queue[0][1] == cpu_cycles:
                frequency = queue.popleft()[0]
                heapq.heappush(max_heap, frequency)

        return cpu_cycles
        