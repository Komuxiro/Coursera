n = int(input())
m = int(input())
k = int(input())
bar = n * m
if 0 < k < bar and (n >= 1 or m >= 1) and (k % n == 0 or k % m == 0):
    print('YES')
else:
    print('NO')
