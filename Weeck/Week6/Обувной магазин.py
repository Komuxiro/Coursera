a = int(input())
b = list(map(int, input().split()))
c = 0
d = 0  # счетчик пар
b.sort()
for i in range(len(b)):
    if b[i] < a:  # если текущее число из списка меньше 'a' то продолжаем
        continue
    elif b[i] == c:
        continue
    elif b[i] == a:
        d += 1
        c = b[i]
    elif b[i] - c >= 3:
        d += 1
        c = b[i]
print(d)
