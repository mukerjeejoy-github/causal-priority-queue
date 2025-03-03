import heapq
import time
from sortedcontainers import SortedDict
from typing import List, Tuple, Any

# Standard Python Heap-based Priority Queue (Min-Heap)
class StandardPriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0  # To maintain order in case of same priority
    
    def add_task(self, task: Any, priority: int) -> None:
        heapq.heappush(self.heap, (priority, self.counter, task))
        self.counter += 1
    
    def pop_task(self) -> Tuple[Any, int]:
        if self.heap:
            priority, _, task = heapq.heappop(self.heap)
            return task, priority
        raise KeyError("pop from an empty priority queue")
    
    def bulk_add_tasks(self, tasks: List[Tuple[Any, int]]) -> None:
        for task, priority in tasks:
            self.add_task(task, priority)

# SortedDict-based Priority Queue
class SortedDictPriorityQueue:
    def __init__(self):
        self.queue = SortedDict()
    
    def add_task(self, task: Any, priority: int) -> None:
        if priority not in self.queue:
            self.queue[priority] = []
        self.queue[priority].append(task)
    
    def pop_task(self) -> Tuple[Any, int]:
        if not self.queue:
            raise KeyError("pop from an empty priority queue")
        min_priority = next(iter(self.queue))
        task = self.queue[min_priority].pop(0)
        if not self.queue[min_priority]:
            del self.queue[min_priority]
        return task, min_priority

    def bulk_add_tasks(self, tasks: List[Tuple[Any, int]]) -> None:
        for task, priority in tasks:
            self.add_task(task, priority)

# Generating Benchmark Data
tasks = [(f"Task {i}", i % 10) for i in range(10000)]  # 10,000 tasks with repeating priorities

# CausalPriorityQueue Setup
cpq = CausalPriorityQueue()
standard_pq = StandardPriorityQueue()
sorted_dict_pq = SortedDictPriorityQueue()

# Benchmark CausalPriorityQueue
start_time = time.time()
cpq.bulk_add_tasks([(t, p, None, 1) for t, p in tasks])
for _ in range(5000):
    cpq.pop_task()
cpq_time = time.time() - start_time

# Benchmark Standard Heap-based Priority Queue
start_time = time.time()
standard_pq.bulk_add_tasks(tasks)
for _ in range(5000):
    standard_pq.pop_task()
std_pq_time = time.time() - start_time

# Benchmark SortedDict Priority Queue
start_time = time.time()
sorted_dict_pq.bulk_add_tasks(tasks)
for _ in range(5000):
    sorted_dict_pq.pop_task()
sorted_dict_pq_time = time.time() - start_time

# Results
benchmark_results = {
    "CausalPriorityQueue": cpq_time,
    "StandardPriorityQueue (heapq)": std_pq_time,
    "SortedDictPriorityQueue": sorted_dict_pq_time
}

benchmark_results
