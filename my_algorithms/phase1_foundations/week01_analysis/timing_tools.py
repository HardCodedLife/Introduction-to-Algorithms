"""
Algorithm Timing and Performance Measurement Tools

Provides utilities for measuring algorithm performance with high precision
and statistical analysis of running times.
"""

import time
import statistics
from typing import Callable, List, Tuple, Any
from functools import wraps


class AlgorithmTimer:
    """High-precision timer for algorithm performance measurement."""
    
    def __init__(self):
        self.measurements = []
    
    def time_function(self, func: Callable, *args, **kwargs) -> float:
        """
        Time a single execution of a function.
        
        Args:
            func: Function to time
            *args: Arguments to pass to function
            **kwargs: Keyword arguments to pass to function
            
        Returns:
            Execution time in seconds
        """
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        self.measurements.append(execution_time)
        return execution_time
    
    def average_time(self, func: Callable, runs: int = 10, *args, **kwargs) -> Tuple[float, float]:
        """
        Time function multiple times and return average and standard deviation.
        
        Args:
            func: Function to time
            runs: Number of runs to average
            *args: Arguments to pass to function
            **kwargs: Keyword arguments to pass to function
            
        Returns:
            Tuple of (average_time, standard_deviation)
        """
        times = []
        for _ in range(runs):
            execution_time = self.time_function(func, *args, **kwargs)
            times.append(execution_time)
        
        avg_time = statistics.mean(times)
        std_dev = statistics.stdev(times) if len(times) > 1 else 0.0
        return avg_time, std_dev
    
    def benchmark_input_sizes(self, func: Callable, input_generator: Callable, 
                            sizes: List[int], runs: int = 5) -> List[Tuple[int, float, float]]:
        """
        Benchmark function across different input sizes.
        
        Args:
            func: Function to benchmark
            input_generator: Function that generates input of given size
            sizes: List of input sizes to test
            runs: Number of runs per size
            
        Returns:
            List of (size, average_time, std_dev) tuples
        """
        results = []
        for size in sizes:
            input_data = input_generator(size)
            avg_time, std_dev = self.average_time(func, runs, input_data)
            results.append((size, avg_time, std_dev))
        return results
    
    def clear_measurements(self):
        """Clear all stored measurements."""
        self.measurements.clear()


def timer_decorator(runs: int = 1):
    """
    Decorator for timing function calls.
    
    Args:
        runs: Number of times to run the function for averaging
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            timer = AlgorithmTimer()
            if runs == 1:
                execution_time = timer.time_function(func, *args, **kwargs)
                print(f"{func.__name__} executed in {execution_time:.6f} seconds")
                return func(*args, **kwargs)
            else:
                avg_time, std_dev = timer.average_time(func, runs, *args, **kwargs)
                print(f"{func.__name__} average: {avg_time:.6f}s (±{std_dev:.6f}s) over {runs} runs")
                return func(*args, **kwargs)
        return wrapper
    return decorator


class ComplexityAnalyzer:
    """Analyze empirical time complexity of algorithms."""
    
    @staticmethod
    def estimate_complexity(sizes: List[int], times: List[float]) -> str:
        """
        Estimate the time complexity based on input sizes and execution times.
        
        Args:
            sizes: List of input sizes
            times: List of corresponding execution times
            
        Returns:
            Estimated complexity as string
        """
        if len(sizes) != len(times) or len(sizes) < 2:
            return "Insufficient data"
        
        # Calculate ratios for different complexity hypotheses
        ratios = []
        for i in range(1, len(sizes)):
            n1, n2 = sizes[i-1], sizes[i]
            t1, t2 = times[i-1], times[i]
            
            if t1 > 0:  # Avoid division by zero
                ratio = t2 / t1
                size_ratio = n2 / n1
                ratios.append((ratio, size_ratio))
        
        if not ratios:
            return "Unable to determine"
        
        # Analyze patterns
        avg_ratio = sum(r[0] for r in ratios) / len(ratios)
        avg_size_ratio = sum(r[1] for r in ratios) / len(ratios)
        
        # Compare with expected ratios for different complexities
        if abs(avg_ratio - 1) < 0.1:
            return "O(1) - Constant"
        elif abs(avg_ratio - avg_size_ratio) < 0.2:
            return "O(n) - Linear"
        elif abs(avg_ratio - (avg_size_ratio ** 2)) < 0.3:
            return "O(n²) - Quadratic"
        elif abs(avg_ratio - (avg_size_ratio * (avg_size_ratio.bit_length()))) < 0.3:
            return "O(n log n) - Linearithmic"
        else:
            return f"Complex pattern (ratio: {avg_ratio:.2f})"


# Example usage functions for testing
def constant_time_example(data):
    """O(1) example - access first element."""
    return data[0] if data else None


def linear_time_example(data):
    """O(n) example - sum all elements."""
    return sum(data)


def quadratic_time_example(data):
    """O(n²) example - nested loop."""
    count = 0
    for i in data:
        for j in data:
            count += 1
    return count


def logarithmic_time_example(data):
    """O(log n) example - binary search simulation."""
    n = len(data)
    while n > 1:
        n //= 2
    return n


if __name__ == "__main__":
    # Example usage
    timer = AlgorithmTimer()
    
    # Test with different algorithms
    test_data = list(range(1000))
    
    print("=== Algorithm Timing Examples ===")
    
    # Time constant operation
    const_time = timer.time_function(constant_time_example, test_data)
    print(f"Constant time: {const_time:.6f}s")
    
    # Time linear operation
    linear_time = timer.time_function(linear_time_example, test_data)
    print(f"Linear time: {linear_time:.6f}s")
    
    # Time quadratic operation (with smaller input)
    small_data = list(range(100))
    quad_time = timer.time_function(quadratic_time_example, small_data)
    print(f"Quadratic time: {quad_time:.6f}s")
    
    print("\n=== Complexity Analysis Example ===")
    
    # Analyze linear algorithm complexity
    sizes = [100, 200, 400, 800, 1600]
    def generate_list(size):
        return list(range(size))
    
    results = timer.benchmark_input_sizes(linear_time_example, generate_list, sizes)
    
    times = [result[1] for result in results]
    complexity = ComplexityAnalyzer.estimate_complexity(sizes, times)
    
    print(f"Estimated complexity for linear_time_example: {complexity}")
    
    for size, avg_time, std_dev in results:
        print(f"Size {size}: {avg_time:.6f}s (±{std_dev:.6f}s)")