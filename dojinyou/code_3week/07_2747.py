# https://www.acmicpc.net/problem/2747

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        if n-1 not in cache :
            cache[n-1] = fib(n-1)
        f_n_1 = cache[n-1]
        if n-2 not in cache :
            cache[n-2] = fib(n-2)
        f_n_2 = cache[n-2]
        return f_n_1 + f_n_2
cache = {0:0, 1:1}
print(fib(int(input())))