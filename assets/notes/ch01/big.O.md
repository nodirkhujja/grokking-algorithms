## Big O Notation
**Purpose:** Measures how the number of operations grows as input size increases.

**Key Point:** Shows algorithm speed by growth rate, not seconds.

### Common Run Times (fastest → slowest)
- **O(log n)** - Logarithmic (Binary search)
- **O(n)** - Linear (Simple search)
- **O(n log n)** - Log-linear (Quicksort)
- **O(n²)** - Quadratic (Selection sort)
- **O(n!)** - Factorial (Traveling salesperson)

### Important Rules
- Big O = **worst-case** scenario
- Drop constants: O(2n) → O(n)
- Drop lower terms: O(n + log n) → O(n)

### Growth Example (100 elements)
- O(log n): ~7 operations
- O(n): 100 operations
- O(n²): 10,000 operations
