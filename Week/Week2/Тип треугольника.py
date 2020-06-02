a = int(input())
b = int(input())
c = int(input())
x = a ** 2
y = b ** 2
z = c ** 2
if a <= 0 or b <= 0 or c <= 0:
    print('impossible')
elif a >= b + c or b >= a + c or c >= a + b:
    print('impossible')
elif x == y + z or y == x + z or z == x + y:
    print('rectangular')
elif a == b == c:
    print('acute')
elif a > b and a > c and x < y + z:
    print('acute')
elif b > a and b > c and y < x + z:
    print('acute')
elif c > a and c > b and z < x + y:
    print('acute')
elif a > b and a > c and x > y + z:
    print('obtuse')
elif b > a and b > c and y > x + z:
    print('obtuse')
elif c > a and c > b and z > x + y:
    print('obtuse')
else:
    print('impossible')
