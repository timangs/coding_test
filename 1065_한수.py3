import sys
aint = int(sys.stdin.readline())
alist = [i for i in range(1,aint+1)]
strlist = [str(i) for i in alist]
chlist = []
#print(strlist)
for i in strlist:
#    print(i)
    if len(i) <= 2:
        chlist.append(int(i))
    else:
        chlst = list(str(i))
        gongcha = int(chlst[0])-int(chlst[1])
        #print(gongcha)
        if len(i) > 2:
            gongcha2 = int(chlst[1]) - int(chlst[2])
            if gongcha2 == gongcha:
                chlist.append(int(i))
print(len(chlist))