from functools import lru_cache

@lru_cache()
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def func1(x):
    # Максимум минимум 
    return (3 * x - x ** 3)

def func2(x):
    # Максимум
    return (9 - x ** 2) / (x ** 2 + 2 * x + 3)

def fib(func, a, b, n=15):
    x1 = a + fibonacci(n-2) / fibonacci(n) * (b - a)
    x2 = a + fibonacci(n-1) / fibonacci(n) * (b - a)
    y1 = func(x1)
    y2 = func(x2)
    k = 1

    while 1:
        if y1 > y2:
            a = x1
            x1 = x2
            x2 = a + fibonacci(n-k-1)/fibonacci(n-k)*(b - a)
        else:
            b = x2
            x2 = x1
            x1 = a + fibonacci(n-k-2)/fibonacci(n-k)*(b - a)
        k += 1
        if k == n - 2:
            break
        
    return (b + a)/2, func((b + a)/2)

max_x, max_y = fib(func1, -2, 0,5)
print("Точка максимума:", max_x, max_y)


min_x, min_y = fib(func2, -3, 3)
print("Точка минимума:", min_x, min_y)