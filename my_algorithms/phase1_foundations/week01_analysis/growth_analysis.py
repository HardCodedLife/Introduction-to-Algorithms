"""
Function Growth Analysis Tools

Tools for comparing and analyzing the growth rates of functions,
particularly useful for understanding asymptotic behavior.
"""

import math
from typing import List, Callable, Dict, Tuple
import matplotlib.pyplot as plt
import numpy as np


class GrowthFunction:
    """Represents a mathematical function for growth analysis."""
    
    def __init__(self, name: str, func: Callable[[float], float], color: str = 'blue'):
        self.name = name
        self.func = func
        self.color = color
    
    def evaluate(self, x: float) -> float:
        """Evaluate function at given point."""
        try:
            return self.func(x)
        except (OverflowError, ZeroDivisionError, ValueError):
            return float('inf')
    
    def evaluate_range(self, x_values: List[float]) -> List[float]:
        """Evaluate function over a range of values."""
        return [self.evaluate(x) for x in x_values]


class GrowthComparator:
    """Compare growth rates of different functions."""
    
    def __init__(self):
        self.functions = {}
        self._setup_common_functions()
    
    def _setup_common_functions(self):
        """Setup common complexity functions."""
        self.functions = {
            'constant': GrowthFunction('O(1)', lambda n: 1, 'red'),
            'logarithmic': GrowthFunction('O(log n)', lambda n: math.log(n) if n > 0 else 0, 'orange'),
            'linear': GrowthFunction('O(n)', lambda n: n, 'green'),
            'linearithmic': GrowthFunction('O(n log n)', lambda n: n * math.log(n) if n > 0 else 0, 'blue'),
            'quadratic': GrowthFunction('O(n²)', lambda n: n ** 2, 'purple'),
            'cubic': GrowthFunction('O(n³)', lambda n: n ** 3, 'brown'),
            'exponential': GrowthFunction('O(2ⁿ)', lambda n: 2 ** min(n, 50), 'red'),  # Cap to prevent overflow
            'factorial': GrowthFunction('O(n!)', lambda n: math.factorial(int(min(n, 20))), 'black')  # Cap to prevent overflow
        }
    
    def add_function(self, name: str, func: Callable[[float], float], display_name: str = None, color: str = 'gray'):
        """Add a custom function for comparison."""
        display_name = display_name or name
        self.functions[name] = GrowthFunction(display_name, func, color)
    
    def compare_growth_rates(self, n_max: int = 100, step: int = 1) -> Dict[str, List[float]]:
        """
        Compare growth rates of all functions.
        
        Args:
            n_max: Maximum value of n to evaluate
            step: Step size for evaluation
            
        Returns:
            Dictionary mapping function names to their values
        """
        x_values = list(range(1, n_max + 1, step))
        results = {'x': x_values}
        
        for name, func in self.functions.items():
            results[name] = func.evaluate_range(x_values)
        
        return results
    
    def plot_growth_comparison(self, n_max: int = 100, step: int = 1, 
                             log_scale: bool = True, functions: List[str] = None):
        """
        Plot growth comparison of functions.
        
        Args:
            n_max: Maximum n value
            step: Step size
            log_scale: Use logarithmic y-axis
            functions: List of function names to plot (None for all)
        """
        x_values = list(range(1, n_max + 1, step))
        
        plt.figure(figsize=(12, 8))
        
        functions_to_plot = functions or list(self.functions.keys())
        
        for name in functions_to_plot:
            if name in self.functions:
                func = self.functions[name]
                y_values = func.evaluate_range(x_values)
                
                # Filter out infinite values for plotting
                valid_points = [(x, y) for x, y in zip(x_values, y_values) 
                              if not math.isinf(y) and y < 1e10]
                
                if valid_points:
                    x_valid, y_valid = zip(*valid_points)
                    plt.plot(x_valid, y_valid, label=func.name, color=func.color, linewidth=2)
        
        plt.xlabel('Input Size (n)')
        plt.ylabel('Time/Operations')
        plt.title('Growth Rate Comparison of Common Complexity Functions')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        if log_scale:
            plt.yscale('log')
            plt.ylabel('Time/Operations (log scale)')
        
        plt.tight_layout()
        plt.show()
    
    def find_crossover_point(self, func1_name: str, func2_name: str, 
                           max_n: int = 1000) -> Tuple[int, float, float]:
        """
        Find where one function overtakes another.
        
        Args:
            func1_name: Name of first function
            func2_name: Name of second function
            max_n: Maximum n to search
            
        Returns:
            Tuple of (crossover_point, func1_value, func2_value)
        """
        if func1_name not in self.functions or func2_name not in self.functions:
            raise ValueError("Function not found")
        
        func1 = self.functions[func1_name]
        func2 = self.functions[func2_name]
        
        for n in range(1, max_n + 1):
            val1 = func1.evaluate(n)
            val2 = func2.evaluate(n)
            
            if val1 > val2 and not math.isinf(val1) and not math.isinf(val2):
                return n, val1, val2
        
        return -1, 0, 0  # No crossover found


class AsymptoticAnalyzer:
    """Analyze asymptotic behavior of empirical data."""
    
    @staticmethod
    def fit_to_known_complexity(sizes: List[int], times: List[float]) -> Dict[str, float]:
        """
        Fit empirical data to known complexity functions.
        
        Args:
            sizes: List of input sizes
            times: List of corresponding times
            
        Returns:
            Dictionary of complexity names and their R² values
        """
        if len(sizes) != len(times) or len(sizes) < 2:
            return {}
        
        # Convert to numpy arrays for easier computation
        n_values = np.array(sizes, dtype=float)
        t_values = np.array(times, dtype=float)
        
        # Define complexity functions to test
        complexity_funcs = {
            'O(1)': lambda n: np.ones_like(n),
            'O(log n)': lambda n: np.log(n),
            'O(n)': lambda n: n,
            'O(n log n)': lambda n: n * np.log(n),
            'O(n²)': lambda n: n ** 2,
            'O(n³)': lambda n: n ** 3
        }
        
        results = {}
        
        for name, func in complexity_funcs.items():
            try:
                # Get expected values from complexity function
                expected_values = func(n_values)
                
                # Calculate R² (coefficient of determination)
                # First normalize both arrays to handle different scales
                if np.std(expected_values) > 0 and np.std(t_values) > 0:
                    correlation = np.corrcoef(expected_values, t_values)[0, 1]
                    r_squared = correlation ** 2 if not np.isnan(correlation) else 0
                    results[name] = r_squared
                else:
                    results[name] = 0
                    
            except (ValueError, FloatingPointError, OverflowError):
                results[name] = 0
        
        return results
    
    @staticmethod
    def predict_performance(sizes: List[int], times: List[float], 
                          target_size: int) -> Dict[str, float]:
        """
        Predict performance at target size based on empirical data.
        
        Args:
            sizes: Historical input sizes
            times: Historical execution times
            target_size: Size to predict performance for
            
        Returns:
            Dictionary of predicted times for different complexities
        """
        if not sizes or not times or len(sizes) != len(times):
            return {}
        
        # Find best fit complexity
        fits = AsymptoticAnalyzer.fit_to_known_complexity(sizes, times)
        
        predictions = {}
        
        # Use the last data point as reference
        ref_size = sizes[-1]
        ref_time = times[-1]
        
        # Calculate growth factor for each complexity
        growth_factors = {
            'O(1)': 1,
            'O(log n)': math.log(target_size) / math.log(ref_size) if ref_size > 1 else 1,
            'O(n)': target_size / ref_size,
            'O(n log n)': (target_size * math.log(target_size)) / (ref_size * math.log(ref_size)) if ref_size > 1 else target_size,
            'O(n²)': (target_size / ref_size) ** 2,
            'O(n³)': (target_size / ref_size) ** 3
        }
        
        for complexity, factor in growth_factors.items():
            predictions[complexity] = ref_time * factor
        
        return predictions


# Example usage and testing
if __name__ == "__main__":
    # Create growth comparator
    comparator = GrowthComparator()
    
    print("=== Growth Rate Analysis Example ===")
    
    # Compare growth rates
    results = comparator.compare_growth_rates(n_max=50)
    
    print("\nGrowth rates for n=10:")
    for name, func in comparator.functions.items():
        value = func.evaluate(10)
        if not math.isinf(value):
            print(f"{func.name}: {value:.2f}")
    
    print("\nGrowth rates for n=20:")
    for name, func in comparator.functions.items():
        value = func.evaluate(20)
        if not math.isinf(value) and value < 1e6:
            print(f"{func.name}: {value:.2f}")
    
    # Find crossover points
    print("\n=== Crossover Points ===")
    crossover = comparator.find_crossover_point('linear', 'logarithmic')
    if crossover[0] > 0:
        print(f"Linear overtakes logarithmic at n={crossover[0]}")
    
    crossover = comparator.find_crossover_point('quadratic', 'linearithmic')
    if crossover[0] > 0:
        print(f"Quadratic overtakes n log n at n={crossover[0]}")
    
    # Test asymptotic analysis
    print("\n=== Asymptotic Analysis Example ===")
    
    # Simulate quadratic algorithm data
    test_sizes = [10, 20, 40, 80, 160]
    test_times = [size ** 2 * 0.001 for size in test_sizes]  # Simulated quadratic times
    
    fits = AsymptoticAnalyzer.fit_to_known_complexity(test_sizes, test_times)
    print("R² values for different complexities:")
    for complexity, r_squared in sorted(fits.items(), key=lambda x: x[1], reverse=True):
        print(f"{complexity}: {r_squared:.4f}")
    
    # Predict performance
    predictions = AsymptoticAnalyzer.predict_performance(test_sizes, test_times, 320)
    print(f"\nPredicted times for n=320:")
    for complexity, pred_time in predictions.items():
        if pred_time < 1e6:  # Filter out unrealistic predictions
            print(f"{complexity}: {pred_time:.6f}s")