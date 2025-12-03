# CLRS Answer Template

## Chapter 2: Getting Started

**Date Started**: September 12, 2025  
**Date Completed**: [Date]  
**Time Spent**: [Hours]

---

## Section 2.1: Insertion Sort

### Section Summary
- **Key Concepts**: 
  - Loop invariants (initialization, maintenance, termination)
  - Insertion sort algorithm and its correctness
  - Linear search and binary search concepts
  - Binary integer addition
  
- **Important Algorithms**: 
  - Insertion sort
  - Linear search
  - Binary integer addition
  
- **Time Complexities**: 
  - Insertion sort: O(n²) worst case, O(n) best case
  - Linear search: O(n)
  
- **Space Complexities**: 
  - Insertion sort: O(1) additional space
  - Linear search: O(1) additional space

### Exercises

#### Exercise 2.1-1
**Problem Statement**: Using Figure 2.2 as a model, illustrate the operation of INSERTION-SORT on an array initially containing the sequence ⟨31, 41, 59, 26, 41, 58⟩.

**Solution**:
```  
Initial: ⟨31, 41, 59, 26, 41, 58⟩
     ---------↑-----------------
      sorted|key|unsorted

Step 1:  ⟨31, 41, 59, 26, 41, 58⟩
         ---------↑--------------
          sorted |key| unsorted

Step 2:  ⟨31, 41, 59, 26, 41, 58⟩
         -------------↑-----------
           sorted   |key|unsorted

Step 3:  ⟨31, 41, 59, 26, 41, 58⟩  ← key=26, shift elements
         -------------↑-----------
         ⟨26, 31, 41, 59, 41, 58⟩  ← after insertion
         ---------------↑--------

Step 4:  ⟨26, 31, 41, 59, 41, 58⟩  ← key=41, shift elements  
         -----------------↑--------
         ⟨26, 31, 41, 41, 59, 58⟩  ← after insertion
         -------------------↑-----

Step 5:  ⟨26, 31, 41, 41, 59, 58⟩  ← key=58, shift elements
         ---------------------↑-----
         ⟨26, 31, 41, 41, 58, 59⟩  ← SORTED!
         -----------------------
```
---

#### Exercise 2.1-2
**Problem Statement**: Consider the procedure SUM-ARRAY on the facing page. It computes the sum of the n numbers in array A[1:n]. State a loop invariant for this procedure, and use its initialization, maintenance, and termination properties to show that the SUM-ARRAY procedure returns the sum of the numbers in A[1:n].

```
SUM-ARRAY(A, n)
1 sum = 0
2 for i = 1 to n
3     sum = sum + A[i]
4 return sum
```

**Solution**:
The *sum* variable is the sum of the sub array of A.   Initialization: It is true prior to the first iteration of the loop. *sum* is initialize to 0, which is true that it is the sum of sub array because sub array is currently empty.
Maintenance: The first iteration shows *sum* = *sum* + A[1], now the sub array is A[1] and *sum* holds the sum of it. Then the second iteration *sum* = *sum* + A[2] shows that *sum* holds the sum of the sub array A[1:2]. So, this property holds for A[1:*i*].
Termination: The loop variable *i* starts at 1 and increases by 1 in each iteration. Once *i*'s value exceeds *n*, the loop terminates, that's when *i* equals *n*+1. When the loop terminates, the *sum* is the sum of sub array A[1:*n*].This property holds.

**Claude's Review:**

**Strengths:**
- You correctly identified the three required properties (initialization, maintenance, termination)
- The basic intuition is correct - tracking the sum of processed elements
- You understand the loop termination condition

**Areas for Improvement:**

1. **Loop Invariant Statement**: You need to state the loop invariant more precisely. A better formulation would be:
   > "At the start of each iteration of the for loop, `sum` equals the sum of elements A[1] through A[i-1]"

2. **Initialization Proof**: Your explanation is correct but could be clearer:
   > "Prior to the first iteration (i=1), the invariant states that sum equals the sum of A[1] through A[0], which is the empty sum = 0. Since sum is initialized to 0, the invariant holds."

3. **Maintenance Proof**: Your logic is right but the explanation could be more rigorous:
   > "Assume the invariant holds at the start of iteration i (sum = A[1]+...+A[i-1]). During iteration i, we execute sum = sum + A[i], so sum becomes A[1]+...+A[i-1]+A[i] = A[1]+...+A[i]. At the start of iteration i+1, the invariant correctly states sum equals A[1] through A[i]."

4. **Termination Analysis**: You're correct about when termination occurs, but the final conclusion could be stronger:
   > "The loop terminates when i = n+1. At termination, the invariant tells us sum = A[1]+...+A[n], which is exactly what we wanted to prove."

**Overall Grade: B+** - You demonstrate good understanding of loop invariants but need more precision in mathematical statements and proof structure.

---

#### Exercise 2.1-3
**Problem Statement**: Rewrite the INSERTION-SORT procedure to sort into monotonically decreasing instead of monotonically increasing order.

**Solution**:  
```
INSERTION-SORT(A, n)  
for i = 2 to n  
  key = A[i]  
  j = i - 1
  while j > 0 and A[j] > key
    A[j + 1] = A[j]
    j = j - 1
    A[j + 1] = key
```

**Algorithm**:
```python
def insertion_sort_decreasing(arr):
    """
    Sort array in decreasing order using insertion sort.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    # Implementation
    pass
```

---

#### Exercise 2.1-4
**Problem Statement**: Consider the **searching problem**:

**Input:** A sequence of n numbers ⟨a₁, a₂, ..., aₙ⟩ stored in array A[1:n] and a value x.

**Output:** An index i such that x equals A[i] or the special value NIL if x does not appear in A.

Write pseudocode for linear search, which scans through the array from beginning to end, looking for x. Using a loop invariant, prove that your algorithm is correct. Make sure that your loop invariant fulfills the three necessary properties.

**Solution**:
[Your detailed solution here]

**Algorithm**:
```python
def linear_search(arr, x):
    """
    Linear search for element x in array.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Implementation
    pass
```

---

#### Exercise 2.1-5
**Problem Statement**: Consider the problem of adding two n-bit binary integers a and b, stored in two n-element arrays A[0:n-1] and B[0:n-1], where each element is either 0 or 1, a = Σᵢ₌₀ⁿ⁻¹ A[i]·2ⁱ, and b = Σᵢ₌₀ⁿ⁻¹ B[i]·2ⁱ. The sum c = a + b of the two integers should be stored in binary form in an (n+1)-element array C[0:n], where c = Σᵢ₌₀ⁿ C[i]·2ⁱ. Write a procedure ADD-BINARY-INTEGERS that takes as input arrays A and B, along with the length n, and returns array C holding the sum.

**Solution**:
[Your detailed solution here]

**Algorithm**:
```python
def add_binary_integers(A, B, n):
    """
    Add two n-bit binary integers represented as arrays.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Implementation
    pass
```

---

## Section 2.2: Analyzing Algorithms

### Section Summary
- **Key Concepts**: 
  - Algorithm analysis and asymptotic notation
  - Best-case, average-case, and worst-case analysis
  - Selection sort algorithm
  - Θ-notation usage

- **Important Algorithms**: 
  - Selection sort
  - Linear search analysis

- **Time Complexities**: 
  - Selection sort: Θ(n²) for all cases
  - Linear search average case: Θ(n)

- **Space Complexities**: 
  - Selection sort: O(1) additional space

### Exercises

#### Exercise 2.2-1
**Problem Statement**: Express the function n³/1000 + 100n² - 100n + 3 in terms of Θ-notation.

**Solution**:
[Your detailed solution here]

---

#### Exercise 2.2-2
**Problem Statement**: Consider sorting n numbers stored in array A[1:n] by first finding the smallest element of A[1:n] and exchanging it with the element in A[1]. Then find the smallest element of A[2:n], and exchange it with A[2]. Then find the smallest element of A[3:n], and exchange it with A[3]. Continue in this manner for the first n-1 elements of A. Write pseudocode for this algorithm, which is known as **selection sort**. What loop invariant does this algorithm maintain? Why does it need to run for only the first n-1 elements, rather than for all n elements? Give the worst-case running time of selection sort in Θ-notation. Is the best-case running time any better?

**Solution**:
[Your detailed solution here]

**Algorithm**:
```python
def selection_sort(arr):
    """
    Sort array using selection sort algorithm.
    Time Complexity: Θ(n²)
    Space Complexity: O(1)
    """
    # Implementation
    pass
```

---

#### Exercise 2.2-3
**Problem Statement**: Consider linear search again (see Exercise 2.1-4). How many elements of the input array need to be checked on the average, assuming that the element being searched for is equally likely to be any element in the array? How about in the worst case? Using Θ-notation, give the average-case and worst-case running times of linear search. Justify your answers.

**Solution**:
[Your detailed solution here]

---

#### Exercise 2.2-4
**Problem Statement**: How can you modify any sorting algorithm to have a good best-case running time?

**Solution**:
[Your detailed solution here]

---

## Section 2.3: Designing Algorithms

### Section Summary
- **Key Concepts**: 
  - Divide-and-conquer approach
  - Merge sort algorithm and analysis
  - Recursive algorithm design
  - Binary search
  - Recurrence relations

- **Important Algorithms**: 
  - Merge sort
  - Binary search
  - Recursive insertion sort

- **Time Complexities**: 
  - Merge sort: Θ(n lg n)
  - Binary search: Θ(lg n)

- **Space Complexities**: 
  - Merge sort: Θ(n) additional space
  - Binary search: O(1) iterative, O(lg n) recursive

### Exercises

#### Exercise 2.3-1
**Problem Statement**: Using Figure 2.4 as a model, illustrate the operation of merge sort on an array initially containing the sequence ⟨3, 41, 52, 26, 38, 57, 9, 49⟩.

**Solution**:
[Your detailed solution here]

---

#### Exercise 2.3-2
**Problem Statement**: The test in line 1 of the MERGE-SORT procedure reads "if p ≥ r" rather than "if p ≠ r." If MERGE-SORT is called with p > r, then the subarray A[p:r] is empty. Argue that as long as the initial call of MERGE-SORT(A, 1, n) has n ≥ 1, the test "if p ≠ r" suffices to ensure that no recursive call has p > r.

**Solution**:
[Your detailed solution here]

---

#### Exercise 2.3-3
**Problem Statement**: State a loop invariant for the while loop of lines 12-18 of the MERGE procedure. Show how to use it, along with the while loops of lines 20-23 and 24-27, to prove that the MERGE procedure is correct.

**Solution**:
[Your detailed solution here]

---

#### Exercise 2.3-4
**Problem Statement**: Use mathematical induction to show that when n ≥ 2 is an exact power of 2, the solution of the recurrence

T(n) = {
  2             if n = 2,
  2T(n/2) + n   if n > 2
}

is T(n) = n lg n.

**Solution**:
[Your detailed solution here]

---

#### Exercise 2.3-5
**Problem Statement**: You can also think of insertion sort as a recursive algorithm. In order to sort A[1:n], recursively sort the subarray A[1:n-1] and then insert A[n] into the sorted subarray A[1:n-1]. Write pseudocode for this recursive version of insertion sort. Give a recurrence for its worst-case running time.

**Solution**:
[Your detailed solution here]

**Algorithm**:
```python
def recursive_insertion_sort(arr, n):
    """
    Recursive implementation of insertion sort.
    Time Complexity: O(n²)
    Space Complexity: O(n) due to recursion stack
    """
    # Implementation
    pass
```

---

#### Exercise 2.3-6
**Problem Statement**: Referring back to the searching problem (see Exercise 2.1-4), observe that if the subarray being searched is already sorted, the searching algorithm can check the midpoint of the subarray against v and eliminate half of the subarray from further consideration. The **binary search** algorithm repeats this procedure, halving the size of the remaining portion of the subarray each time. Write pseudocode, either iterative or recursive, for binary search. Argue that the worst-case running time of binary search is Θ(lg n).

**Solution**:
[Your detailed solution here]

**Algorithm**:
```python
def binary_search(arr, x):
    """
    Binary search for element x in sorted array.
    Time Complexity: Θ(lg n)
    Space Complexity: O(1) iterative, O(lg n) recursive
    """
    # Implementation
    pass
```

---

#### Exercise 2.3-7
**Problem Statement**: The while loop of lines 5-7 of the INSERTION-SORT procedure in Section 2.1 uses a linear search to scan (backward) through the sorted subarray A[1:j-1]. What if insertion sort used a binary search (see Exercise 2.3-6) instead of a linear search? Would that improve the overall worst-case running time of insertion sort to Θ(n lg n)?

**Solution**:
[Your detailed solution here]

---

#### Exercise 2.3-8
**Problem Statement**: Describe an algorithm that, given a set S of n integers and another integer x, determines whether S contains two elements that sum to exactly x. Your algorithm should take Θ(n lg n) time in the worst case.

**Solution**:
[Your detailed solution here]

**Algorithm**:
```python
def two_sum_exists(S, x):
    """
    Determine if two elements in S sum to x.
    Time Complexity: Θ(n lg n)
    Space Complexity: O(1) additional space
    """
    # Implementation
    pass
```

---

## Chapter 2 Problems

### Problem 2-1: Insertion sort on small arrays in merge sort
**Problem Statement**: Although merge sort runs in Θ(n lg n) worst-case time and insertion sort runs in Θ(n²) worst-case time, the constant factors in insertion sort can make it faster in practice for small problem sizes on many machines. Thus it makes sense to coarsen the leaves of the recursion by using insertion sort within merge sort when subproblems become sufficiently small. Consider a modification to merge sort in which n/k sublists of length k are sorted using insertion sort and then merged using the standard merging mechanism, where k is a value to be determined.

a. Show that insertion sort can sort the n/k sublists, each of length k, in Θ(nk) worst-case time.

b. Show how to merge the sublists in Θ(n lg(n/k)) worst-case time.

c. Given that the modified algorithm runs in Θ(nk + n lg(n/k)) worst-case time, what is the largest value of k as a function of n for which the modified algorithm has the same running time as standard merge sort, in terms of Θ-notation?

d. How should you choose k in practice?

**Solution**:
[Comprehensive solution with detailed explanation]

---

### Problem 2-2: Correctness of bubblesort
**Problem Statement**: Bubblesort is a popular, but inefficient, sorting algorithm. It works by repeatedly swapping adjacent elements that are out of order. The procedure BUBBLESORT sorts array A[1:n].

```
BUBBLESORT(A, n)
1 for i = 1 to n - 1
2     for j = n downto i + 1
3         if A[j] < A[j - 1]
4             exchange A[j] with A[j - 1]
```

a. Let A' denote the array A after BUBBLESORT(A, n) is executed. To prove that BUBBLESORT is correct, you need to prove that it terminates and that A'[1] ≤ A'[2] ≤ ⋯ ≤ A'[n]. In order to show that BUBBLESORT actually sorts, what else do you need to prove?

b. State precisely a loop invariant for the for loop in lines 2-4, and prove that this loop invariant holds.

c. Using the termination condition of the loop invariant proved in part (b), state a loop invariant for the for loop in lines 1-4 that allows you to prove inequality (2.5).

d. What is the worst-case running time of BUBBLESORT? How does it compare with the running time of INSERTION-SORT?

**Solution**:
[Comprehensive solution with detailed explanation]

**Implementation**:
```python
def bubblesort(arr):
    """
    Bubblesort implementation.
    Time Complexity: Θ(n²)
    Space Complexity: O(1)
    """
    # Implementation
    pass
```

---

### Problem 2-3: Correctness of Horner's rule
**Problem Statement**: You are given the coefficients a₀, a₁, a₂, ..., aₙ of a polynomial P(x) = Σₖ₌₀ⁿ aₖxᵏ = a₀ + a₁x + a₂x² + ⋯ + aₙ₋₁xⁿ⁻¹ + aₙxⁿ, and you want to evaluate this polynomial for a given value of x. **Horner's rule** says to evaluate the polynomial according to this parenthesization: P(x) = a₀ + x(a₁ + x(a₂ + ⋯ + x(aₙ₋₁ + xaₙ)⋯)).

The procedure HORNER implements Horner's rule to evaluate P(x), given the coefficients a₀, a₁, a₂, ..., aₙ in an array A[0:n] and the value of x.

```
HORNER(A, n, x)
1 p = 0
2 for i = n downto 0
3     p = A[i] + x · p
4 return p
```

a. In terms of Θ-notation, what is the running time of this procedure?

b. Write pseudocode to implement the naive polynomial-evaluation algorithm that computes each term of the polynomial from scratch. What is the running time of this algorithm? How does it compare with HORNER?

c. Consider the following loop invariant for the procedure HORNER: At the start of each iteration of the for loop of lines 2-3, p = Σₖ₌₀ⁿ⁻⁽ⁱ⁺¹⁾ A[k + i + 1] · xᵏ. Interpret a summation with no terms as equaling 0. Following the structure of the loop-invariant proof presented in this chapter, use this loop invariant to show that, at termination, p = Σₖ₌₀ⁿ A[k] · xᵏ.

**Solution**:
[Comprehensive solution with detailed explanation]

**Implementation**:
```python
def horner_evaluation(coefficients, x):
    """
    Evaluate polynomial using Horner's rule.
    Time Complexity: Θ(n)
    Space Complexity: O(1)
    """
    # Implementation
    pass

def naive_polynomial_evaluation(coefficients, x):
    """
    Naive polynomial evaluation.
    Time Complexity: Θ(n²)
    Space Complexity: O(1)
    """
    # Implementation
    pass
```

---

### Problem 2-4: Inversions
**Problem Statement**: Let A[1:n] be an array of n distinct numbers. If i < j and A[i] > A[j], then the pair (i, j) is called an **inversion** of A.

a. List the five inversions of the array ⟨2, 3, 8, 6, 1⟩.

b. What array with elements from the set {1, 2, ..., n} has the most inversions? How many does it have?

c. What is the relationship between the running time of insertion sort and the number of inversions in the input array? Justify your answer.

d. Give an algorithm that determines the number of inversions in any permutation on n elements in Θ(n lg n) worst-case time. (Hint: Modify merge sort.)

**Solution**:
[Comprehensive solution with detailed explanation]

**Implementation**:
```python
def count_inversions(arr):
    """
    Count inversions in array using modified merge sort.
    Time Complexity: Θ(n lg n)
    Space Complexity: Θ(n)
    """
    # Implementation
    pass
```

---

## Personal Notes & Insights

### Key Takeaways
- [Important insights from this chapter]
- [Connections to previously learned material]
- [Real-world applications]

### Challenging Concepts
- [Concepts that were difficult to understand]
- [How you overcame the challenges]

### Implementation Notes
- [Python-specific considerations]
- [Performance optimization tips]
- [Common pitfalls to avoid]

### Questions for Further Study
- [Unresolved questions]
- [Topics to explore deeper]
- [Related algorithms to investigate]

---

## Study Progress

### Exercises Completed: 0/16
- [ ] Exercise 2.1-1: Insertion sort trace
- [ ] Exercise 2.1-2: SUM-ARRAY loop invariant
- [ ] Exercise 2.1-3: Decreasing insertion sort
- [ ] Exercise 2.1-4: Linear search with loop invariant
- [ ] Exercise 2.1-5: Binary integer addition
- [ ] Exercise 2.2-1: Θ-notation for polynomial
- [ ] Exercise 2.2-2: Selection sort analysis
- [ ] Exercise 2.2-3: Linear search average case
- [ ] Exercise 2.2-4: Best-case optimization
- [ ] Exercise 2.3-1: Merge sort trace
- [ ] Exercise 2.3-2: Merge sort base case
- [ ] Exercise 2.3-3: Merge procedure correctness
- [ ] Exercise 2.3-4: Merge sort recurrence proof
- [ ] Exercise 2.3-5: Recursive insertion sort
- [ ] Exercise 2.3-6: Binary search implementation
- [ ] Exercise 2.3-7: Binary search in insertion sort
- [ ] Exercise 2.3-8: Two-sum problem

### Problems Completed: 0/4
- [ ] Problem 2-1: Hybrid merge-insertion sort
- [ ] Problem 2-2: Bubblesort correctness
- [ ] Problem 2-3: Horner's rule analysis
- [ ] Problem 2-4: Inversion counting

### Self-Assessment
**Understanding Level**: [1-5 scale with explanation]
**Implementation Confidence**: [1-5 scale with explanation]
**Areas Needing Review**: [List specific topics]

---

## References & Resources

### Textbook Sections
- Section 2.1: Insertion Sort (Pages 18-24)
- Section 2.2: Analyzing Algorithms (Pages 25-31)
- Section 2.3: Designing Algorithms (Pages 31-43)

### Additional Resources Used
- [Online resources, papers, etc.]
- [Supplementary materials]

### Code Repository
- Implementation files: [File paths]
- Test files: [File paths]
- Benchmark results: [File paths]

---

*Template Usage Instructions*:
1. Copy this template for each chapter
2. Fill in all bracketed placeholders
3. Complete exercises in order
4. Update progress regularly
5. Review and revise answers before moving to next chapter