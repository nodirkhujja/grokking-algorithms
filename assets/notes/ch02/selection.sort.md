# 📦 CHAPTER 2: ARRAYS & LINKED LISTS
**Core Concept:** Two ways to store lists in memory

### 1. Arrays
**Structure:** Elements stored in **contiguous** memory locations (side by side).

**Operations:**
- **Reading:** O(1) - instant access to any element
- **Insertion:** O(n) - may need to move everything
- **Deletion:** O(n) - may need to shift elements

**Key Points:**
- Fast reads (random access)
- Slow inserts (need contiguous space)
- Fixed size (may need to resize and move all elements)

*Note: When array is full, you need to find new space for all elements.*

### 2. Linked Lists
**Structure:** Each element stores the item + pointer to next element.

**Operations:**
- **Reading:** O(n) - must traverse from start
- **Insertion:** O(1) - just change pointers
- **Deletion:** O(1) - just change pointers

**Key Points:**
- Slow reads (sequential access only)
- Fast inserts/deletes (just update pointers)
- Dynamic size (elements anywhere in memory)

### 3. Arrays vs Linked Lists

| Operation | Arrays | Linked Lists |
|-----------|--------|--------------|
| Reading | O(1) | O(n) |
| Insertion | O(n) | O(1) |
| Deletion | O(n) | O(1) |

**When to use:**
- **Arrays:** Random access, known size, reading > inserting
- **Linked Lists:** Frequent inserts/deletes, dynamic size

### 4. Selection Sort
**Strategy:** Find smallest element, add to new array, repeat.

**Performance:**
- **Time Complexity:** O(n²)

*Note: You check n elements, then n-1, then n-2... = n × n/2 operations*
