# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.


def factorial(n):
    factorial_result = 1
    while n > 1:
        factorial_result *= n
        n -= 1
    return factorial_result


# print factorial(4)
# >>> 24
# print factorial(5)
# >>> 120
# print factorial(6)
# >>> 720

print(factorial(4))

print(factorial(5))

print(factorial(6))
