num = int(input())
num1 = ((num - (num % 10)) // 10) // 10
num2 = num % 10
num3 = (num - (num % 10)) // 10 % 10
print(num1 + num2 + num3)
