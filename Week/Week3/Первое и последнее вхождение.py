a = input('')
b = a.find('f')
c = a.rfind('f')
if b == -1:
    print()
elif b == c:
    print(c)
else:
    print(b, c)
