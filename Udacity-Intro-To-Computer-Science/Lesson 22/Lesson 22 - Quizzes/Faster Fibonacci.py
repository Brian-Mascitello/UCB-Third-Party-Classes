# Define a faster fibonacci procedure that will enable us to computer
# fibonacci(36).


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        old_fib, result_fib = 1, 1
        while n > 2:
            old_fib, result_fib = result_fib, result_fib + old_fib
            n -= 1
        return result_fib


# print fibonacci(36)
# >>> 14930352

for x in range(0, 37):
    print(str(x) + ': ' + str(fibonacci(x)))
