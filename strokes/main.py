def p1():
    n = int(input())
    stroke = ''
    for i in range(n):
        p = input()
        stroke += p
    print(stroke)
def p2():
    try:
        s = input()
        s = list(s.lower())
        a = s.index('a')
        b = s.index('b')
        if a > b:
            print('B')
        else:
            print('A')
    except ValueError:
        print('Error!')
def p3():
    i = input()
    i = list(i)
    rep = input()
    rep = rep.split(' ')
    for j in i:
        if rep[0] == j:
            i[i.index(j)] = rep[1]
    print(''.join(i))
def p4():
    u = input()
    res = []
    for i in u:
        if i == 'а':
            res += i+'я'
        else:
            res += i
    print(''.join(res))
def p5():
    o = input()
    print(len(o))
    p = ''
    for i in o:
        if i.isdigit() == False:
            p += i
    print(p)
def p6():
    y = input()
    y = y.split(' ')
    max = 0
    for i in y:
        if len(i) > max:
            max = len(i)
    biggest = []
    for i in y:
        if len(i) == max:
            biggest.append(i)
    print(' '.join(biggest))
p6()