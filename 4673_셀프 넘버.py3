mresult = [i for i in range(1,10001)]
result = []
for i in mresult:
    t = list((str(i)))
    for j in t:
        i += int(j)
    if i <= 10000:
        result.append(i)
alist = list(set(mresult)-set(result))
alist.sort()
for i in alist:
    print(i)
