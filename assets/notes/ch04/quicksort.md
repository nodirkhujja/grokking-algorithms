# 🐍 CHAPTER 4: QUICKSORT

**Core Strategy:** Divide & Conquer (D&C)

### 1. The Strategy (How it works)
1.  **Pick a Pivot:** In this step, we use the **first element** of the array.
2.  **Partition:** - Find all elements **smaller** than the pivot → `less` sub-array.
    - Find all elements **larger** than the pivot → `greater` sub-array.
3.  **Recurse:** Call `quicksort` on the sub-arrays and combine them:
    `quicksort(less) + [pivot] + quicksort(greater)`

### 2. The Base Case
- An array with **0** elements (empty).
- An array with **1** element.
*Logic: These are already "sorted" by nature.*

### 3. The Big O Performance
- **Average Case:** O(nlogn)
- **Worst Case:** O(n^2) this is same as **selection sort**
*Note: The worst case happens when we pick the first element as pivot on an already sorted array.*
