a = list(map(int, input().split()))
for i in range(len(a)):
    if a[i] == max(a):
        print(max(a), i)
