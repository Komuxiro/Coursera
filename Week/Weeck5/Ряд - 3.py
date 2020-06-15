n = int(input())
min_n = 10**(n-1) - 1
max_n = 10 ** n - 1
print(*tuple(range(max_n, min_n, -2)))
