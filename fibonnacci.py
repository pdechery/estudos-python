# The Fibonacci sequence is a mathematical sequence in which each number
# is the sum of the two preceding numbers, where 0 and 1 are the first two numbers
# https://realpython.com/fibonacci-sequence-python/#getting-started-with-the-fibonacci-sequence
def fibonacci_of(num):
  if num in {0, 1}:
    return num
  return fibonacci_of(num-2) + fibonacci_of(num-1)


cache = {0: 0, 1: 1}


def fibonacci_of_memoization(n):
    '''
    Example with "memoization" (caching). 
    Avoid redundant function calls so better algorithm
    '''
    if n in cache:  # Base case
        return cache[n]
    # Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]


# https://realpython.com/fibonacci-sequence-python/#getting-started-with-the-fibonacci-sequence

def fibonacci_of(n):
    # Validate the value of n
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    # Handle the base cases
    if n in {0, 1}:
        return n

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number


if __name__ == '__main__':

  print([fibonacci_of(n) for n in range(9)])

