inFile = open('Text 1.txt', 'r', encoding='utf8')
line = inFile.readlines()
a = {}
for i in line:
    school, ball = map(int, line.split()[-2:])
    if school in a:
        a[school][0] += 1
        a[school][1] += ball
    else:
        a[school] = [1, ball]

    print(a)
inFile.close()
