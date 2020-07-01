a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = set(a) & set(b)
print(sorted(c))
