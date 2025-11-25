def sum(number1, number2):
    return number1 + number2
def multiply(number1, number2):
    return number1 * number2    
def subtract(number1, number2):
    return number1 - number2    
def divide(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        return "Error! Division by zero."
def modulus(number1, number2):
    return number1 % number2        
def power(base, exponent):
    return base ** exponent             
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

    
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    