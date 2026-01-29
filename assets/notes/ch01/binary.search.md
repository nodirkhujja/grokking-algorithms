# 🔍 CHAPTER 1: BINARY SEARCH & BIG O

## 1. Binary Search
**Core Idea:** Eliminate half the search space with each guess.

**Requirement:** List must be **sorted**.

### How It Works
1. Start with the **middle element**.
2. If guess is **too low** → eliminate lower half.
3. If guess is **too high** → eliminate upper half.
4. Repeat until found.

### Performance
- **Simple Search:** O(n) - check every element
- **Binary Search:** O(log n) - eliminate half each time

*Example: Phone book with 240,000 names*
- Simple search: 240,000 steps max
- Binary search: 18 steps max

