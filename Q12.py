# 12. Create a decorator that measures and prints the execution time of a function.

import time
from functools import wraps

def time_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time  # Calculate execution time
        print(f"Execution time of '{func.__name__}': {execution_time:.4f} seconds")
        return result  # Return the result of the original function
    return wrapper

# Example usage
@time_logger
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

if __name__ == "__main__":
    result = example_function(1000000)
    print(f"Result: {result}")
