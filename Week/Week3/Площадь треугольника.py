a = float(input())
b = float(input())
c = float(input())
# use the Heron formula
sqr1 = (a+b+c) * 0.5
sqr2 = (sqr1*(sqr1-a)*(sqr1-b)*(sqr1-c))**0.5
print(sqr2)
