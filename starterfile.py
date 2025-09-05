"""
Math Utilities Project
Collaborative coding assignment using GitHub workflow
"""

# Placeholder functions (contributors will implement them)

def function1():
    # Contributor 1 will implement
    pass

def function2(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    # Contributor 2 implemented prime checkin
    # Contributor 3 will implement

def fibonacci_sequence(n: int) -> int:
   
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return 0
    if n == 1:
        return 1
     
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def function3():
    
    print(f"Fibonacci of 10 is: {fibonacci_sequence(10)}")
    return fibonacci_sequence(10)



def function4(a, b):
    """
    Compute the Greatest Common Divisor (GCD) of two integers
    using the Euclidean algorithm.
    Handles zero and negative values correctly.
    """
    a, b = abs(a), abs(b)  # GCD should always be non-negative

    if a == 0 and b == 0:
        return 0  # or raise ValueError("GCD(0,0) is undefined")

    while b != 0:
        a, b = b, a % b
    return a



# Driver (Admin will finalize later)
if __name__ == "__main__":
    print("Math Utilities Project Running...")
    # Admin will call all contributed functions here
