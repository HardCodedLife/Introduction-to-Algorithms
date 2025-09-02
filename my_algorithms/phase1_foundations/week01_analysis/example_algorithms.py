"""
Example Algorithms for Complexity Analysis

A collection of algorithms with different time complexities
for testing and learning purposes.
"""

import random
import math
from typing import List, Any


class ExampleAlgorithms:
    """Collection of algorithms with known time complexities."""
    
    @staticmethod
    def constant_time_access(data: List[Any], index: int = 0) -> Any:
        """
        O(1) - Constant time algorithm.
        Access element at specific index.
        
        Args:
            data: Input list
            index: Index to access
            
        Returns:
            Element at specified index
        """
        return data[index] if 0 <= index < len(data) else None
    
    @staticmethod
    def linear_search(data: List[int], target: int) -> int:
        """
        O(n) - Linear time algorithm.
        Search for target in unsorted list.
        
        Args:
            data: List to search
            target: Value to find
            
        Returns:
            Index of target or -1 if not found
        """
        for i, value in enumerate(data):
            if value == target:
                return i
        return -1
    
    @staticmethod
    def binary_search(data: List[int], target: int) -> int:
        """
        O(log n) - Logarithmic time algorithm.
        Search for target in sorted list.
        
        Args:
            data: Sorted list to search
            target: Value to find
            
        Returns:
            Index of target or -1 if not found
        """
        left, right = 0, len(data) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if data[mid] == target:
                return mid
            elif data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    @staticmethod
    def simple_sort(data: List[int]) -> List[int]:
        """
        O(n²) - Quadratic time algorithm.
        Simple bubble sort implementation.
        
        Args:
            data: List to sort
            
        Returns:
            Sorted list
        """
        result = data.copy()
        n = len(result)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        
        return result
    
    @staticmethod
    def merge_sort(data: List[int]) -> List[int]:
        """
        O(n log n) - Linearithmic time algorithm.
        Merge sort implementation.
        
        Args:
            data: List to sort
            
        Returns:
            Sorted list
        """
        if len(data) <= 1:
            return data.copy()
        
        mid = len(data) // 2
        left = ExampleAlgorithms.merge_sort(data[:mid])
        right = ExampleAlgorithms.merge_sort(data[mid:])
        
        return ExampleAlgorithms._merge(left, right)
    
    @staticmethod
    def _merge(left: List[int], right: List[int]) -> List[int]:
        """Helper function for merge sort."""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    @staticmethod
    def cubic_algorithm(data: List[int]) -> int:
        """
        O(n³) - Cubic time algorithm.
        Triple nested loop counting.
        
        Args:
            data: Input list
            
        Returns:
            Count of operations
        """
        count = 0
        n = len(data)
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    count += 1
        
        return count
    
    @staticmethod
    def fibonacci_recursive(n: int) -> int:
        """
        O(2ⁿ) - Exponential time algorithm.
        Naive recursive Fibonacci.
        
        Args:
            n: Fibonacci number to calculate
            
        Returns:
            nth Fibonacci number
        """
        if n <= 1:
            return n
        return (ExampleAlgorithms.fibonacci_recursive(n - 1) + 
                ExampleAlgorithms.fibonacci_recursive(n - 2))
    
    @staticmethod
    def fibonacci_iterative(n: int) -> int:
        """
        O(n) - Linear time algorithm.
        Iterative Fibonacci calculation.
        
        Args:
            n: Fibonacci number to calculate
            
        Returns:
            nth Fibonacci number
        """
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b
    
    @staticmethod
    def matrix_multiplication_naive(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        """
        O(n³) - Cubic time algorithm.
        Naive matrix multiplication.
        
        Args:
            a: First matrix
            b: Second matrix
            
        Returns:
            Product matrix
        """
        rows_a, cols_a = len(a), len(a[0])
        rows_b, cols_b = len(b), len(b[0])
        
        if cols_a != rows_b:
            raise ValueError("Matrix dimensions don't match for multiplication")
        
        result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
        
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += a[i][k] * b[k][j]
        
        return result


class DataGenerator:
    """Generate test data for algorithm analysis."""
    
    @staticmethod
    def random_list(size: int, min_val: int = 1, max_val: int = 1000) -> List[int]:
        """Generate random list of integers."""
        return [random.randint(min_val, max_val) for _ in range(size)]
    
    @staticmethod
    def sorted_list(size: int, min_val: int = 1, max_val: int = 1000) -> List[int]:
        """Generate sorted list of integers."""
        return sorted(DataGenerator.random_list(size, min_val, max_val))
    
    @staticmethod
    def reverse_sorted_list(size: int, min_val: int = 1, max_val: int = 1000) -> List[int]:
        """Generate reverse-sorted list of integers."""
        return sorted(DataGenerator.random_list(size, min_val, max_val), reverse=True)
    
    @staticmethod
    def nearly_sorted_list(size: int, swaps: int = None) -> List[int]:
        """Generate nearly sorted list with few random swaps."""
        if swaps is None:
            swaps = max(1, size // 20)  # 5% swaps by default
        
        data = list(range(1, size + 1))
        
        for _ in range(swaps):
            i, j = random.randint(0, size - 1), random.randint(0, size - 1)
            data[i], data[j] = data[j], data[i]
        
        return data
    
    @staticmethod
    def square_matrix(size: int, min_val: int = 1, max_val: int = 10) -> List[List[int]]:
        """Generate square matrix of integers."""
        return [[random.randint(min_val, max_val) for _ in range(size)] 
                for _ in range(size)]


# Example usage and demonstrations
if __name__ == "__main__":
    print("=== Algorithm Complexity Examples ===\n")
    
    # Test data
    small_data = DataGenerator.random_list(100)
    sorted_data = DataGenerator.sorted_list(100)
    
    print("1. Constant Time - Array Access:")
    result = ExampleAlgorithms.constant_time_access(small_data, 50)
    print(f"Element at index 50: {result}")
    
    print("\n2. Linear Time - Linear Search:")
    target = small_data[25]  # Ensure target exists
    index = ExampleAlgorithms.linear_search(small_data, target)
    print(f"Found {target} at index {index}")
    
    print("\n3. Logarithmic Time - Binary Search:")
    target = sorted_data[25]
    index = ExampleAlgorithms.binary_search(sorted_data, target)
    print(f"Found {target} at index {index}")
    
    print("\n4. Quadratic Time - Bubble Sort:")
    unsorted = [64, 34, 25, 12, 22, 11, 90]
    sorted_result = ExampleAlgorithms.simple_sort(unsorted)
    print(f"Original: {unsorted}")
    print(f"Sorted: {sorted_result}")
    
    print("\n5. Linearithmic Time - Merge Sort:")
    merge_sorted = ExampleAlgorithms.merge_sort(unsorted)
    print(f"Merge sorted: {merge_sorted}")
    
    print("\n6. Linear vs Exponential - Fibonacci:")
    n = 10
    fib_iterative = ExampleAlgorithms.fibonacci_iterative(n)
    fib_recursive = ExampleAlgorithms.fibonacci_recursive(n)
    print(f"Fibonacci({n}) - Iterative: {fib_iterative}, Recursive: {fib_recursive}")
    
    print("\n7. Cubic Time - Matrix Multiplication:")
    matrix_a = DataGenerator.square_matrix(3, 1, 5)
    matrix_b = DataGenerator.square_matrix(3, 1, 5)
    product = ExampleAlgorithms.matrix_multiplication_naive(matrix_a, matrix_b)
    print(f"Matrix A: {matrix_a[0]}")
    print(f"          {matrix_a[1]}")
    print(f"          {matrix_a[2]}")
    print(f"Matrix B: {matrix_b[0]}")
    print(f"          {matrix_b[1]}")
    print(f"          {matrix_b[2]}")
    print(f"Product:  {product[0]}")
    print(f"          {product[1]}")
    print(f"          {product[2]}")
    
    print("\n=== Data Generation Examples ===")
    print(f"Random list (10): {DataGenerator.random_list(10)}")
    print(f"Sorted list (10): {DataGenerator.sorted_list(10)}")
    print(f"Nearly sorted (10): {DataGenerator.nearly_sorted_list(10)}")