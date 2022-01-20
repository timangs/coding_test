import sys
intext = [list(sys.stdin.readline().strip()) for i in range(int(sys.stdin.readline().strip().lower()))]
result=[]
for i,j in enumerate(intext):
    for k,l in enumerate(j):
        try:
            if k == 0:
                result.append(list(j[0]))
                if j[k] != j[k + 1]:
                    result[i].append(j[k + 1])
            elif j[k] != j[k+1]:
                result[i].append(j[k+1])
        except:
            pass
count = 0
for i in result:
    if len(i) == len(set(i)):
        count += 1
print(count)