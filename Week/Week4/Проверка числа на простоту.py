n = int(input())


def isPrime(n):
    if n == 2 or n == 3:
        return 'YES'
    if n % 2 == 0 or n < 2:
        return 'NO'
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return 'NO'

    return 'YES'


print(isPrime(n))
