i = input('Не кратные:')
i = i.split(' ')
i = list(map(int, i))
r = input('Кратные:')
r = r.split(' ')
r = list(map(int, r))
min = int(input())
max = int(input())
res = []
isdiv = True
for j in range(min, max+1):
    for k in i:
        if j % k == 0:
            isdiv = False
            break
        else:
            continue
    if isdiv != False:
        for o in r:
            if j % o == 0:
                res.append(j)
    isdiv = True
print(res)
print(len(res))