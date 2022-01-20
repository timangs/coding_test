
import sys


a= int(sys.stdin.readline().strip())
b=[0 for i in range(int(a)*2)]
result=[]
for i in range(2,len(b)):
    if b[i] == 0:
        b[i]= 2
        for j in range(i,len(b),i):
            if b[j] == 2:
                result.append(j)
            else:
                b[j] = 1
if a == 1:
    print("6")
for i in result:
    if a < i*result[result.index(i)+1]:
        print(i*result[result.index(i)+1])
        break