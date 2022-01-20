import sys
#import time

a,b = map(int,sys.stdin.readline().strip().split())

#start_time = time.time()

c = [0 for i in range(b+1)]

for i in range(2,b+1):
    if c[i] == 0:
        c[i]=2
        for j in range(i,len(c),i):
            if c[j] == 2 and j >= a:
                print(j)
            else:
                c[j] = 1
