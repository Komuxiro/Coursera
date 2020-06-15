a = input()
a1 = a[a.find('h') + 1:a.rfind('h')]
a1 = a1.replace('h', 'H')
print(a[:a.find('h') + 1] + a1 + a[a.rfind('h'):])
