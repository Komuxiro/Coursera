a = list(map(int, input().split()))
b = int(input())
pos = 0
while pos < len(a) and a[pos] >= b:
    pos += 1
print(pos + 1)
