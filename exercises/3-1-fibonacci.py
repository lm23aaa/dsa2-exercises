from time import perf_counter

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

def fib_dynamic(number, memo):
    if len(memo) > number and memo[number] != None:
        return memo[number]
    
    if number < 0:
        return -1
    elif number == 0 or number == 1:
        memo.insert(number, number)
        return number
    else:
        curr = fibonacci(number - 2) + fibonacci(number - 1)
        memo.insert(number, curr)
        return curr
    
def fib_ground_up(number):
    if number < 0:
        return -1
    elif number == 0 or number == 1:
        return number
    
    memo = [1, 1]
    for n in range(2, number + 1):
        memo.insert(n, memo[n - 2] + memo[n - 1])
    
    return memo[number]

def fib_timer(number, type = 'rec'):
    start = perf_counter()
    
    if type == 'rec':
        fibonacci(number)
    elif type == 'dyn':
        memo = []
        fib_dynamic(number, memo)
    else:
        fib_ground_up(number)
        
    stop = perf_counter()
    
    print(stop - start)

fib_timer(35)
fib_timer(35, 'dyn')
fib_timer(35, 'gro')