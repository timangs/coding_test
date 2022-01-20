import sys
input_cycle = int(sys.stdin.readline().strip())
for a in range(input_cycle):
    i,v = sys.stdin.readline().split()
    distence = int(v)-int(i)
    first = 0
    countc = 0
    n = 1
    while True:
        if distence <= first:
            print(f'{countc}')
            break
        else:
            first += n
            if distence <= first:
                countc += 1
                print(f'{countc}')
                break
            else:
                first += n
                countc += 2
        n+=1