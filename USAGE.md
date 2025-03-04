# **Causal Priority Queue (CPQ) - Usage Guide**

## **Introduction**
The **Causal Priority Queue (CPQ)** is a dynamic priority queue that allows tasks to **influence each other's priorities** based on predefined **causal relationships**. Unlike traditional priority queues, CPQ **automatically adjusts priorities** in real-time, making it highly effective for use cases such as **task scheduling, AI decision-making, financial trading, healthcare triage, and cybersecurity.**

This guide will walk you through installing, using, and understanding CPQ with detailed examples.

---

##  Installation
CPQ is available as a Python package and can be installed via **PyPI**:

```bash
pip install causal-priority-queue
```

Once installed, you can import it in your Python scripts:

```python
from causal-priority-queue import CausalPriorityQueue
```

---

##  CPQ Operations
The following operations can be performed using CPQ:

###  Adding Tasks
Use `add_task()` to insert a task with an optional influence on other tasks:

```python
cpq = CausalPriorityQueue()
cpq.add_task("Task A", priority=3)
cpq.add_task("Task B", priority=1)
cpq.add_task("Task C", priority=5)
```

🔹 **Task priorities remain static** if no dependencies are specified.

###  Adding Tasks with Dependencies (Causal Influence)
A task can influence another task’s priority by specifying `influences` and `influence_weight`:

```python
cpq.add_task("A: Submit Report", priority=5, influences=["B: Review Report"], influence_weight=2)
cpq.add_task("B: Review Report", priority=3)
```

🔹 If **Task A is completed**, **Task B’s priority increases** automatically by 2.

###  Removing Tasks
To remove a task manually before it's processed:

```python
cpq.remove_task("Task A")
```

🔹 The task is removed from the queue, and dependencies remain unaffected.

###  Popping (Processing) Tasks
Tasks are retrieved based on their priority using `pop_task()`:

```python
print("Popped task:", cpq.pop_task())
```

🔹 The **task with the highest priority is returned**, and dependent task priorities are adjusted.

###  Bulk Adding Tasks
You can add multiple tasks efficiently using `bulk_add_tasks()`:

```python
cpq.bulk_add_tasks([
    ("Task 1", 5, None, 1),
    ("Task 2", 2, ["Task 3"], 1),
    ("Task 3", 7, None, 1),
])
```

🔹 This method optimizes task insertion and is useful for **batch processing.**

###  Viewing All Tasks
To check the queue state:

```python
print("Current Tasks:", cpq.get_tasks())
```

🔹 Returns all tasks sorted by **priority**.

###  Clearing the Queue
To reset the queue completely:

```python
cpq.clear_queue()
```

🔹 This **removes all tasks and dependencies** from the queue.

---

##  Mathematical Foundation of CPQ
CPQ is built upon a **mathematical model that integrates priority queuing with causal graph theory**. The core mathematical principles include:

###  Priority Function
Each task in CPQ is assigned a priority P<sub>t</sub>, and when a dependent task is processed, its priority is updated based on the influence weight.

#### Priority Update Equation:

<div align="center">
    P<sub>new</sub> = max(P<sub>old</sub> + w, 0)
</div>

Where:
- (P<sub>new</sub>) is the updated priority after influence adjustment.
- (P<sub>old</sub>) is the previous priority of the dependent task.
- (w) is the influence weight applied by the completed task.
- The **max function ensures** that priority never becomes negative.

###  Influence Graph Representation
The **causal relationships** between tasks form a **directed influence graph**, represented as a weighted adjacency list:

<div align="center">
    G = (V, E)
</div>

Where:
- \( V \) represents tasks.
- \( E \) represents directed edges, where edge weights indicate the **influence magnitude** between tasks.

###  Heap-Based Priority Extraction
CPQ maintains a **Min-Heap** (or Max-Heap for descending order processing), ensuring an **O(log n)** retrieval time for the highest-priority task. This allows efficient task execution while dynamically adjusting dependencies.

###  Complexity Analysis
| Operation            | Complexity |
|---------------------|------------|
| Insert Task         | O(log n)   |
| Remove Task         | O(log n)   |
| Pop Task            | O(log n)   |
| Adjust Priorities   | O(k log n) |
| Bulk Insert         | O(m log n) |

Where:
- \( n \) is the number of tasks in the queue.
- \( k \) is the number of dependent tasks.
- \( m \) is the number of tasks being inserted in bulk.

---

##  Real-World Use Cases

###  Healthcare: Dynamic Patient Triage
```python
cpq.add_task("Patient A", priority=5, influences=["Patient B"], influence_weight=3)
cpq.add_task("Patient B", priority=2)

print("Before popping:", cpq.get_tasks())
print("Popped:", cpq.pop_task())
print("After popping:", cpq.get_tasks())
```
 **🔹 When Patient A is treated, Patient B’s priority increases, ensuring urgent cases are handled efficiently.**

---

##  Performance Considerations
CPQ introduces a **slight computational overhead** due to its dependency tracking mechanism. However, the benefits of **automatic priority adjustments** outweigh the performance trade-off in **dynamic scheduling, AI, and real-time applications**.

To improve efficiency:
- Use **bulk_add_tasks()** when adding multiple tasks.
- Avoid unnecessary dependencies if they are not required.
- Keep priority updates **within practical bounds** to maintain queue performance.

---

##  Summary & Next Steps
CPQ offers a powerful alternative to static priority queues, making it ideal for **adaptive scheduling and decision-making.**

- **Dynamic priority updates based on causal relationships**
- **Ideal for AI, scheduling, cybersecurity, and financial trading**
- **Mathematically modeled for efficiency**
- **Open-source & easy to use**

##  Install & Try CPQ Today!
```bash
pip install causal-priority-queue
```

 **🔹 Contribute & Explore More:** [GitHub Repository](https://github.com/mukerjeejoy-github/causal-priority-queue)

 **Let me know how CPQ improves your workflows!**

