# 2. fibonacci
# n <  0, return -1 (ERROR CODE)
# n == 0, return 0
# n == 1, return 1
# n >= 2, return fibonacci(n - 2) + fibonacci(n - 1)
def fibonacci(number):
    if number < 0:
        return -1
    elif number == 0 or number == 1:
        return number
    else:
        return fibonacci(number - 2) + fibonacci(number - 1)

# TEST 2.
# i = -5
# while i < 10:
#     print(f"{i}: {fibonacci(i)}")
#     i += 1