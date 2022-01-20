import re
import sys
a = str(sys.stdin.readline().strip().lower())
tokens = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in tokens:
    a = re.sub(i,"a",a)
print(len(a))