# Week 1: Algorithm Analysis Fundamentals
*September 3-9, 2025*

## Learning Objectives
- [ ] Understand the role of algorithms in computing
- [ ] Master asymptotic notation (Big-O, Θ, Ω)
- [ ] Learn to analyze algorithm running times
- [ ] Build intuition for growth of functions

## Study Plan

### Day 1-2: Chapter 1 - The Role of Algorithms in Computing
**Reading Goals:**
- [ ] What are algorithms?
- [ ] Algorithms as a technology
- [ ] Why study algorithms?
- [ ] Real-world applications

**Key Concepts:**
- Algorithm definition
- Efficiency importance
- Scalability concerns
- Algorithm engineering

### Day 3-5: Chapter 3 - Characterizing Running Times
**Reading Goals:**
- [ ] Asymptotic notation fundamentals
- [ ] O-notation (Big-O)
- [ ] Ω-notation (Big-Omega) 
- [ ] Θ-notation (Big-Theta)
- [ ] o-notation and ω-notation

**Key Concepts:**
- Growth of functions
- Worst-case vs average-case analysis
- Best-case analysis
- Asymptotic comparison of functions

### Day 6-7: Implementation and Practice
**Coding Goals:**
- [ ] Build timing measurement utilities
- [ ] Create function growth visualizers
- [ ] Implement asymptotic notation calculator
- [ ] Test with example algorithms

## Implementation Tasks

### Core Utilities
1. **Timer Class**: Precise algorithm timing
2. **Growth Analyzer**: Compare function growth rates
3. **Complexity Calculator**: Determine Big-O from data points
4. **Visualization Tools**: Plot function growth

### Example Implementations
1. **Simple algorithms** with different complexities:
   - O(1) - constant time
   - O(log n) - logarithmic
   - O(n) - linear
   - O(n log n) - linearithmic
   - O(n²) - quadratic
   - O(2ⁿ) - exponential

## Exercises
1. Implement and time algorithms with different complexities
2. Create growth comparison visualizations
3. Practice identifying Big-O from code inspection
4. Analyze recursive algorithm complexities

## Success Criteria
- [ ] Can identify Big-O, Θ, Ω for given algorithms
- [ ] Built working timing and analysis tools
- [ ] Understand when to use each notation
- [ ] Can explain algorithm efficiency trade-offs

## Files Structure
```
week01_analysis/
├── README.md              # This file
├── timing_tools.py        # Algorithm timing utilities
├── growth_analysis.py     # Function growth analysis
├── complexity_calc.py     # Complexity calculation tools
├── visualization.py       # Growth visualization tools
├── example_algorithms.py  # Sample algorithms for testing
├── tests.py              # Unit tests
├── analysis.py           # Performance analysis
└── notes.md              # Personal learning notes
```

## Next Week Preview
Week 2 will focus on mathematical prerequisites and divide-and-conquer foundations, building on the analysis skills developed this week.