a = int(input())


def phib(a):
    if a in (1, 2):
        return 1
    return phib(a - 1) + phib(a - 2)


print(phib(a))
